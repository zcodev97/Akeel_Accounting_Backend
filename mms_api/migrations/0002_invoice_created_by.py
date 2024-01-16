# Generated by Django 4.2.9 on 2024-01-15 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mms_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]