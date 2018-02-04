from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView

from gob.jobs.views import JobListView, JobCreateView

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='jobs'),
    url(r'^login', RedirectView.as_view(
        url=settings.OAUTH_LOGIN_URL, permanent=False)),
    url(r'^add', JobCreateView.as_view(), name='jobs-add')
]
