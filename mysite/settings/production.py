from __future__ import absolute_import, unicode_literals
from .base import *

import os

DEBUG = False

ALLOWED_HOSTS = ['13.238.219.1', 'riaparish.co.nz']

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

try:
    from .local import *
except ImportError:
    pass
