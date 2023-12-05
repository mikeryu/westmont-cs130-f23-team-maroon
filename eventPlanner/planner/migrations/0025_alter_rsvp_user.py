# Generated by Django 4.2.6 on 2023-12-01 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0024_alter_rsvp_user_alter_rsvp_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
