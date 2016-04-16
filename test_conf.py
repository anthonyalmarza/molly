import os
import sys

from django.apps import apps
from django.conf import settings


sys.path.insert(0, os.path.dirname(__file__))


if not settings.configured:

    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'molly',
        ],
        ROOT_URLCONF='',
        DEBUG=False
    )

    apps.populate(settings.INSTALLED_APPS)
