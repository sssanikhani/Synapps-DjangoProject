# Generated by Django 3.1.3 on 2020-11-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_time',
            field=models.DateTimeField(verbose_name='reported'),
        ),
    ]
