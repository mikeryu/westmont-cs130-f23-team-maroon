# Generated by Django 4.2.6 on 2023-12-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0033_remove_rsvp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
