# Generated by Django 4.2.9 on 2024-02-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0018_endpointlog_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawtype',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]