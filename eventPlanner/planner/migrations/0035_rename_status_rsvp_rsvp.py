# Generated by Django 4.2.6 on 2023-12-05 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0034_rsvp_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='status',
            new_name='rsvp',
        ),
    ]
