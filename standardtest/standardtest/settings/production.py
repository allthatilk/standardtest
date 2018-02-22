from __future__ import absolute_import, unicode_literals

# from .base import *

SECRET_KEY = PRODUCTION_SECRET_KEY

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
