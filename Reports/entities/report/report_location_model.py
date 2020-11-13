from django.db import models


class ReportLocation(models.Model):
    pid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)