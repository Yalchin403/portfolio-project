# Generated by Django 2.2.16 on 2020-10-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
