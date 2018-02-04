import os

import dj_database_url

from gob.settings.common import * # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['APP_SECRET_KEY']

DEBUG = False

# Meh
ALLOWED_HOSTS = ['*']

OAUTH_LOGIN_PROVIDER = os.environ['OAUTH_LOGIN_PROVIDER']

if OAUTH_LOGIN_PROVIDER == 'slack':
    SLACK_TEAM_ID = os.environ['SLACK_TEAM_ID']

# TODO:
# /accounts/ is hardcoded here
# this always assumes allauth URLs are set at /accounts/
# any change here should also reflect in main `urls.py`
if OAUTH_LOGIN_PROVIDER == 'reddit':
    OAUTH_LOGIN_URL = '/accounts/reddit/login'
elif OAUTH_LOGIN_PROVIDER == 'slack':
    OAUTH_LOGIN_URL = '/accounts/slack/login'

_db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {}
DATABASES['default'] = {}
DATABASES['default'].update(_db_from_env)

# For Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
