# Generated by Django 4.0 on 2021-12-17 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0007_alter_participantquestionanswer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantquestionanswer',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.participant'),
        ),
    ]
