# Generated by Django 4.2.6 on 2023-11-20 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0017_event_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
    ]
