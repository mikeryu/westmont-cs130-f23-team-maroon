# Generated by Django 4.2.6 on 2023-12-02 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0029_alter_rsvp_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rsvp',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='user',
        ),
    ]