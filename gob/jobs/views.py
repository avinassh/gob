from django.views.generic import ListView
from django.views.generic.edit import CreateView

from gob.jobs.models import Job
from gob.jobs.forms import JobCreateForm


class JobListView(ListView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
