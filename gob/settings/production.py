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

_db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {}
DATABASES['default'] = {}
DATABASES['default'].update(_db_from_env)
