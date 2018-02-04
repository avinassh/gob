from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.http import HttpResponseBadRequest

from gob.jobs.models import Job
from gob.jobs.forms import JobCreateForm


class JobListView(ListView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    form_class = JobCreateForm
    success_url = '/'

    def form_valid(self, form):
        message_url = self._get_message_url()
        if not message_url:
            m = 'Something went wrong, contact site admin'
            return HttpResponseBadRequest(m)
        form.instance.message_url = message_url
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    def _get_message_url(self):
        user_social_account = None
        for social_account in self.request.user.socialaccount_set.all():
            if social_account.provider == settings.OAUTH_LOGIN_PROVIDER:
                user_social_account = social_account
        if not user_social_account:
            return
        if social_account.provider == 'slack':
            uid = social_account.extra_data['user']['id']
            return F"https://{settings.SLACK_TEAM_ID}.slack.com/messages/{uid}"
        elif social_account.provider == 'reddit':
            uid = self.request.user.username
            return F"https://www.reddit.com/message/compose/?to={uid}"
        else:
            return


class JobUpdateView(UpdateView):
    model = Job
    form_class = JobCreateForm
    success_url = '/'
