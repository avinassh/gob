from django.views.generic import ListView

from gob.jobs.models import Job


class JobListView(ListView):
    model = Job
