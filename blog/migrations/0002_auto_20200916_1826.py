# Generated by Django 2.2.16 on 2020-09-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time_pub',
            field=models.DateTimeField(),
        ),
    ]
