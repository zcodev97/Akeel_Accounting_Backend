# Generated by Django 4.2.9 on 2024-02-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0030_companytype'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(default='eebf995c-c4e4-446b-89e2-790eeea213e5', on_delete=django.db.models.deletion.CASCADE, to='mms_api.companytype'),
            preserve_default=False,
        ),
    ]