# Generated by Django 4.2.6 on 2023-12-05 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0032_rsvp_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='user',
        ),
    ]