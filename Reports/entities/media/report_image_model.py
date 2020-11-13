from django.db import models
from Reports.entities.report.report_model import Report
import os
from uuid import uuid4


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class ReportImage(models.Model):
    report = models.ForeignKey(
        to=Report,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='images',
        related_query_name='images'
    )
    file = models.ImageField(upload_to=path_and_rename('report_images'))