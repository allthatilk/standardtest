from __future__ import absolute_import, unicode_literals

from .base import *


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = PRODUCTION_SECRET_KEY

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
