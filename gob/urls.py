"""gob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from importlib import import_module

from django.conf.urls import re_path, include
from django.contrib import admin
from allauth.socialaccount import providers

# Little hack to allow only /accounts/reddit/ and /accounts/slack/ URLs
# from https://github.com/pennersr/django-allauth/blob/0.35.0/allauth/urls.py#L15,#L22  # noqa
prov_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns += getattr(prov_mod, 'urlpatterns', None)


urlpatterns = [
    re_path(r'^', include('gob.jobs.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include(prov_urlpatterns)),
]
