from django.contrib.auth.models import User
from django.db import models

from packs.models import Pack


class WebhookReports(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    name = models.TextField(max_length=100, null=False, blank=False)
    dt = models.DateTimeField(null=False, blank=False)
    mail = models.TextField(max_length=100, null=False, blank=False)
    desc = models.TextField(max_length=100, null=True, blank=True, default='No desc')
    phone_number = models.TextField(max_length=20, null=False, blank=False)
