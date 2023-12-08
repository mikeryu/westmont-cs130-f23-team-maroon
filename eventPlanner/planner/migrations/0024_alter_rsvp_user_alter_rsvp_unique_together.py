# Generated by Django 4.2.6 on 2023-12-01 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0023_rsvp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rsvp',
            unique_together={('user', 'event')},
        ),
    ]
