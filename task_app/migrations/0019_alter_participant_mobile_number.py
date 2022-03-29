# Generated by Django 4.0 on 2022-03-29 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0018_alter_participant_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mobile_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^09[0-9]{9}$', message='شماره ی موبایل معتبر نمیباشد.')]),
        ),
    ]
