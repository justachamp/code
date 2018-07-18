import logging

from datetime import time
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models.loading import get_models, get_apps
from IPython.frontend.terminal.embed import InteractiveShellEmbed
from IPython.config.loader import Config

logger = logging.getLogger('command')


class Command(BaseCommand):
    help = 'Runs django shell with imported all models'

    def handle(self, *args, **options):
        logger.info(self.__class__.help)

        if options.get("print_sql", False):
            # Code from http://gist.github.com/118990
            from django.db.backends import util
            try:
                import sqlparse
            except ImportError:
                has_sqlparse = None

            class PrintQueryWrapper(util.CursorDebugWrapper):
                def execute(self, sql, params=()):
                    starttime = time.time()
                    try:
                        return self.cursor.execute(sql, params)
                    finally:
                        raw_sql = self.db.ops.\
                            last_executed_query(self.cursor, sql, params)
                        execution_time = time.time() - starttime
                        if has_sqlparse:
                            print sqlparse.format(raw_sql, reindent=True)
                        else:
                            print raw_sql
                        print
                        print 'Execution time: %.6fs' % execution_time
                        print

        imported_objects = {'settings': settings}

        model_aliases = getattr(settings, 'SHELL_PLUS_MODEL_ALIASES', {})

        for app_mod in get_apps():
            app_models = get_models(app_mod)
            if not app_models:
                continue

            app_name = app_mod.__name__.split('.')[-2]
            app_aliases = model_aliases.get(app_name, {})
            model_labels = []

            for model in app_models:
                model_name = model.__name__
                try:
                    imported_object = getattr(__import__(app_mod.__name__,
                                                         {}, {},
                                                         model.__name__),
                                              model.__name__)

                    alias = app_aliases.get(model_name, model_name)
                    imported_objects[alias] = imported_object
                    if model_name == alias:
                        model_labels.append(model_name)
                    else:
                        model_labels.append("%s (as %s)" % (model_name, alias))

                    try:
                        name = model._meta.verbose_name.lower()\
                            .replace(' ', '_')
                        pname = model._meta.verbose_name_plural.lower()\
                            .replace(' ', '_')
                    except:
                        name = model_name.lower().replace(' ', '_')
                        pname = name + 's'

                    if 'id' in [f.name for f in model._meta.fields]:
                        all_objs = model.objects.all().order_by('id')[:15]
                    else:
                        all_objs = model.objects.all() \
                            .order_by(model._meta.fields[0].name)[:15]

                    if all_objs:
                        imported_objects[pname] = all_objs
                        for i, obj in enumerate(imported_objects[pname]):
                            iname = "%s_%s" % (name, i + 1)
                            imported_objects[iname] = obj

                except AttributeError, e:
                    print self.style.ERROR(
                        "Failed to import '%s' from '%s' reason: %s"
                        % (model.__name__, app_name, str(e)))

        c = Config()
        c.InteractiveShell.confirm_exit = False
        c.InteractiveShell.autocall = True
        c.InteractiveShellApp.exec_lines = ['%autoreload 2']

        ipshell = InteractiveShellEmbed(
            config=c,
            banner1='%s django shell' % settings.PROJECT_NAME,
            user_ns=imported_objects,
        )
        ipshell.extension_manager.load_extension('autoreload')
        ipshell.run_line_magic('autoreload', '2')
        ipshell()
