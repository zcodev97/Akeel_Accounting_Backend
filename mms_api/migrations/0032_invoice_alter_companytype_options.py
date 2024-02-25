# Generated by Django 4.2.9 on 2024-02-25 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mms_api', '0031_company_company_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_in_dinar', models.FloatField()),
                ('price_in_dollar', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='companytype',
            options={'verbose_name_plural': 'نوع الشركة'},
        ),
    ]
