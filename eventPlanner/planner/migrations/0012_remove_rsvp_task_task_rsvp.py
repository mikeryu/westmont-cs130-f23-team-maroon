# Generated by Django 4.1.7 on 2023-11-13 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0011_alter_rsvp_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='RSVP',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.rsvp'),
        ),
    ]
