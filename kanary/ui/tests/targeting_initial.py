# -*- coding: utf-8 -*-
import re
import csv
from functools import partial

from django.db import transaction
from django.conf import settings

from etc import dimensions
from bidrequest.constants import EXCHANGES
from ui.targeting import models

re_parent = re.compile('.*\((.*?)\)$')


def add_main_categories(content_category):
    """
    Add only parents, first we need them.

    .. note::
        Why we use ``next`` method on ``rows`` value?. Because do not want
        columns' names.
    """
    with open(settings.PROJECT_DIR / "targeting" /
              "csv" / "content_categories" /
              "category_mapping_complete.csv", 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=';')
        rows.next()

        for row in rows:
            (
                iab_category,
                iab_category_name,
                appnexus_category_name,
                appnexus_category
            ) = row

            if appnexus_category == "#N/A":
                continue

            parent = re_parent.findall(appnexus_category_name)

            if parent:
                parent_name = parent[0].strip()
                content_category(name=parent_name)


def add_subcategories(content_category, content_category_value,
                      nexage, smaato, appnexus):
    """
    Add the subcategories. If parent exist, use it. (Tree)
    After added representant, add appnexus and nexage categories.

    .. note::
        Why we use ``next`` method on ``rows`` value?. Because do not want
        columns' names.
    """
    with open(settings.PROJECT_DIR / "targeting" /
              "csv" / "content_categories" /
              "category_mapping_complete.csv", 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=';')
        rows.next()

        for row in rows:
            (
                iab_category,
                iab_category_name,
                appnexus_category_name,
                appnexus_category
            ) = row

            if appnexus_category == "#N/A":
                continue

            parent = re_parent.findall(appnexus_category_name)
            appnexus_category_name = appnexus_category_name\
                .split("(")[0].strip()

            if parent:
                parent_name = parent[0].strip()
                parent_representant = content_category(name=parent_name)[0]
                representant = content_category(name=appnexus_category_name,
                                                parent=parent_representant)[0]
            else:
                representant = content_category(name=appnexus_category_name)[0]

            content_category_value(
                name=appnexus_category.strip(),
                exchange=appnexus,
                representant=representant
            )
            content_category_value(
                name=iab_category.strip(),
                exchange=smaato,
                representant=representant
            )
            content_category_value(
                name=iab_category.strip(),
                exchange=nexage,
                representant=representant
            )


@transaction.atomic
def targeting_initial():
    """
    We use this function for tests to fill database.
    .. warning::
        Always use ``get_or_create`` to consider already existing values.
    """
    TargetValue = models.TargetValue
    ContentCategory = models.ContentCategory
    ContentCategoryValue = models.ContentCategoryValue

    content_category = partial(ContentCategory.objects.get_or_create)
    content_category_value = partial(ContentCategoryValue.objects.get_or_create)

    location = partial(TargetValue.objects.get_or_create, category=dimensions.g_location)
    os = partial(TargetValue.objects.get_or_create, category=dimensions.g_os)
    carrier = partial(TargetValue.objects.get_or_create, category=dimensions.carrier)
    make = partial(TargetValue.objects.get_or_create, category=dimensions.make)
    model = partial(TargetValue.objects.get_or_create, category=dimensions.model)
    gender = partial(TargetValue.objects.get_or_create, category=dimensions.gender)
    age_group = partial(TargetValue.objects.get_or_create, category=dimensions.age_group)
    position = partial(TargetValue.objects.get_or_create, category=dimensions.position)
    inventory = partial(TargetValue.objects.get_or_create, category=dimensions.inventory)
    domain = partial(TargetValue.objects.get_or_create, category=dimensions.domain)

    nexage = EXCHANGES.nexage
    smaato = EXCHANGES.smaato
    appnexus = EXCHANGES.appnexus

    openrtb_exchanges = [nexage, smaato]

    location(value='USA')
    location(value='Germany')

    os(value='Android')
    os(value='Nokia OS')

    carrier(value='WiFi')
    carrier(value='GPRS')

    make(value='Sony')
    make(value='LG')

    model(value='Samsung Galaxy S')
    model(value='Lg Swift L9')

    male = gender(value='Male')[0]
    female = gender(value='Female')[0]
    other = gender(value='Other')[0]
    unspecified = gender(value='Unspecified')[0]

    gender(value='male', exchange=appnexus, representant=male)
    gender(value='female', exchange=appnexus, representant=female)
    gender(value='', exchange=appnexus, representant=unspecified)

    for exchange in openrtb_exchanges:
        gender(value='M', exchange=exchange, representant=male)
        gender(value='F', exchange=exchange, representant=female)
        gender(value='O', exchange=exchange, representant=other)
        gender(value='', exchange=exchange, representant=unspecified)

    age_15 = age_group(value='Under 15', exchange=appnexus)[0]
    age_15_24 = age_group(value='15 to 24', exchange=appnexus)[0]
    age_25_44 = age_group(value='25 to 44', exchange=appnexus)[0]
    age_45_64 = age_group(value='45 to 64', exchange=appnexus)[0]
    age_65 = age_group(value='65 and upwards', exchange=appnexus)[0]
    age_un = age_group(value='Unspecified', exchange=appnexus)[0]

    for exchange in openrtb_exchanges:
        age_group(value='Under 15', exchange=exchange, representant=age_15)
        age_group(value='15 to 24', exchange=exchange, representant=age_15_24)
        age_group(value='25 to 44', exchange=exchange, representant=age_25_44)
        age_group(value='45 to 64', exchange=exchange, representant=age_45_64)
        age_group(value='65 and upwards', exchange=exchange, representant=age_65)
        age_group(value='Unspecified', exchange=exchange, representant=age_un)

    above = position(value='Above the fold')[0]
    below = position(value='Below the fold')[0]
    unknown = position(value='Unknown')[0]
    unspecified = position(value='Unspecified')[0]

    position(value='above', exchange=appnexus, representant=above)
    position(value='below', exchange=appnexus, representant=below)
    position(value='unkown', exchange=appnexus, representant=unknown)
    position(value='', exchange=appnexus, representant=unspecified)

    for exchange in openrtb_exchanges:
        position(value='1', exchange=exchange, representant=above)
        position(value='2', exchange=exchange, representant=unknown)
        position(value='3', exchange=exchange, representant=below)
        position(value='', exchange=exchange, representant=unspecified)

    app = inventory(value='Application')[0]
    web = inventory(value='Web')[0]

    # Add values for Appnexus?
    for exchange in openrtb_exchanges:
        inventory(value='app', exchange=nexage, representant=app)
        inventory(value='site', exchange=nexage, representant=web)

    domain(value='roobwalter.com')
    domain(value='huelhudson.com')
    domain(value='ryanschinner.org')

    add_main_categories(content_category)
    add_subcategories(
        content_category,
        content_category_value,
        nexage,
        smaato,
        appnexus
    )
