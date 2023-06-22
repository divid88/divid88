from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default='django-insecure-m!=zj!7n%s=c$bk26sp!0nt#2o)xzqw()jm_*_nyco@78sop0w')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
