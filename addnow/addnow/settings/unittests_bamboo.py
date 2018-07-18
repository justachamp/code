from .unittests import *

NOSE_ARGS = [
    '--verbosity=2',
    '--detailed-errors',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-html-dir=./var/tests-python/',
    '--cover-package=addnow,addnow.apps.accounts,addnow.apps.dashboard,addnow.apps.reports,addnow.apps.tracker'
]
