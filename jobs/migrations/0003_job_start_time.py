# Generated by Django 2.2.16 on 2021-03-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
