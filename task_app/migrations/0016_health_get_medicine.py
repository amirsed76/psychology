# Generated by Django 4.0 on 2022-02-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0015_alter_image_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='get_medicine',
            field=models.BooleanField(default=False),
        ),
    ]
