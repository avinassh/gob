from django.conf.urls import url
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

from gob.jobs.views import JobListView, JobCreateView, JobUpdateView

app_name = 'jobs'
urlpatterns = [
    url(r'^$', JobListView.as_view(), name='jobs'),
    url(r'^add', login_required(JobCreateView.as_view()), name='jobs-add'),
    url(r'^edit/(?P<pk>[\w-]+)$', login_required(JobUpdateView.as_view()),
        name='edit'),
    # TODO:
    # Move following to user_manager
    url(r'^login', RedirectView.as_view(
        url=settings.OAUTH_LOGIN_URL, permanent=False), name='login'),
]
