from django.db import models
from django.contrib.auth.models import User

from Reports.entities.report.report_type_model import ReportType
from Reports.entities.report.report_location_model import ReportLocation


class Report(models.Model):

    class Meta:
        ordering = ['-report_time',]

    submitter = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='reports',
        related_query_name='reports'
    )
    report_type = models.ForeignKey(
        to=ReportType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='reports',
        related_query_name='reports'
    )
    report_locations = models.ManyToManyField(
        to=ReportLocation,
        related_name='reports',
        related_query_name='reports',
    )

    content = models.CharField(max_length=500)
    report_time = models.DateTimeField()
    requester = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)