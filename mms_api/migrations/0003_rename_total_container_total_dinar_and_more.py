# Generated by Django 4.2.9 on 2024-01-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0002_invoice_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='container',
            old_name='total',
            new_name='total_dinar',
        ),
        migrations.AddField(
            model_name='container',
            name='total_dollar',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]