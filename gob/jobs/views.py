from django.views.generic import ListView
from django.views.generic.edit import CreateView

from gob.jobs.models import Job
from gob.jobs.forms import JobCreateForm


class JobListView(ListView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm

    def form_valid(self, form):
        import ipdb; ipdb.set_trace()

    def form_invalid(self, form):
        import ipdb; ipdb.set_trace()
