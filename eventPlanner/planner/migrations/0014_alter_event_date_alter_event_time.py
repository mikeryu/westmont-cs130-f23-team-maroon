# Generated by Django 4.2.5 on 2023-11-16 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0013_remove_task_rsvp_rsvp_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(max_length=100),
        ),
    ]
