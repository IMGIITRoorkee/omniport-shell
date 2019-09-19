# Generated by Django 2.2.3 on 2019-08-26 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultymember',
            name='employee_id',
            field=models.CharField(default=None, max_length=6, unique=True, validators=[django.core.validators.RegexValidator('\\d{6}')]),
            preserve_default=False,
        ),
    ]
