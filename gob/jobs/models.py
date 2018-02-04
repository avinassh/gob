from django.db import models
from django.contrib.auth.models import User

from gob.utils import TimeStampMixin


class Job(TimeStampMixin):
    title = models.CharField(max_length=80, null=True)
    description = models.TextField(max_length=300)
    company_name = models.CharField(max_length=80, null=True)
    location = models.CharField(max_length=80)
    salary = models.CharField()

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
