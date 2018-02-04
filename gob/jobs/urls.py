from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView

from gob.jobs.views import JobListView, JobCreateView

app_name = 'jobs'
urlpatterns = [
    url(r'^$', JobListView.as_view(), name='jobs'),
    url(r'^add', JobCreateView.as_view(), name='jobs-add'),
    # TODO:
    # Move following to user_manager
    url(r'^login', RedirectView.as_view(
        url=settings.OAUTH_LOGIN_URL, permanent=False), name='login'),
]
