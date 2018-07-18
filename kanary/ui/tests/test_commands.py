import pytest
from django.core import management
from django.conf import settings
from django.db.models.loading import get_models, get_apps
from django.core.exceptions import ImproperlyConfigured
from south.exceptions import NoMigrations
from south.creator.changes import AutoChanges
from south.migration.base import Migrations
from south.creator import freezer

from ui.report.models import ReportAdvert


@pytest.mark.django_db(transaction=True)
@pytest.mark.command
def test_dev_setup(appnexus_api_requests, cdn_api):
    """
    Test preparing kanary to development
    #. drop current database
    #. run syncdb. Since pytest-django turns off south's syncdb command,
        we have to import it manually. Only this overwritten command,
        can sync apps that does not have migrations
    #. migrate database
    #. Check report adverts count - should be none, since they're being created
        in fill_campaigns only
    #. run fill_campaigns and fill_reports command
    #. check number of report adverts
    #. Try to read data from all models.
        If someone will forget about migrations, that's where we'll hit exceptions
    #. Check whether model differs from last migration
    """
    from south.management.commands.syncdb import Command as SyncCommand
    """Run commands as a fresh dev."""
    management.call_command('drop_kanary', interactive=False)
    sync = SyncCommand()
    sync.execute(verbosity=0, database=settings.DATABASES.keys()[0])
    management.call_command('migrate', interactive=False)
    assert ReportAdvert.objects.count() == 0
    management.call_command('fill_campaigns', interactive=False)
    management.call_command('fill_reports', interactive=False)
    assert ReportAdvert.objects.count() > 0

    app_models = []
    for app_mod in get_apps():
        app_models.extend(get_models(app_mod))

    for model in app_models:
        print('Querying for: ' + model.__name__)
        model.objects.first()

    for app in settings.INSTALLED_APPS:
        if app.split('.')[0] == 'ui':
            app = app.split('.')[-1]
            try:
                migrations = Migrations(app, force_creation=False, verbose_creation=False)
            # if there is no migrations directory
            except NoMigrations:
                continue
            # if there are no models
            except ImproperlyConfigured:
                continue

            # if migrations directory is empty
            if not migrations:
                continue

            last_migration = migrations[-1]

            # Two models saved in dictionary, one based migration, second on models.py
            migration_defs = dict(
                (k, v) for k, v in last_migration.migration_class().models.items()
                if k.split(".")[0] == migrations.app_label()
            )
            model_defs = dict(
                (k, v) for k, v in freezer.freeze_apps([migrations.app_label()]).items()
                if k.split(".")[0] == migrations.app_label()
            )
            change_source = AutoChanges(
                migrations=migrations,
                old_defs=migration_defs,
                old_orm=last_migration.orm(),
                new_defs=model_defs,
            )

            assert list(change_source.get_changes()) == []
