from django.db import models
from django.contrib.auth.models import User

from gob.utils import TimeStampMixin


class Job(TimeStampMixin):
    title = models.CharField(max_length=80, null=True)
    description = models.TextField(max_length=300)
    company_name = models.CharField(max_length=80, null=True)
    location = models.CharField(max_length=80)
    salary_start = models.PositiveIntegerField()
    salary_end = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=True)
    message_url = models.URLField()

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return F"{self.id} - {self.description[:10]}"
