from .base import *

DEBUG = False

ALLOWED_HOSTS = ['13.238.219.1', 'riaparish.co.nz'] 

try:
    from .local import *
except ImportError:
    pass
