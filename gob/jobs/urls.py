from django.conf.urls import url

from gob.jobs.views import JobListView

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='jobs'),
    url(r'^jobs', JobListView.as_view(), name='jobs')
]
