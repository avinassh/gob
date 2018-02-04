from django.conf.urls import url

from gob.jobs.views import JobListView, JobCreateView

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='jobs'),
    url(r'^add', JobCreateView.as_view(), name='jobs-add')
]
