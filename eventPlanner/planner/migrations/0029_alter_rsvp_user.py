# Generated by Django 4.2.6 on 2023-12-02 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0028_alter_rsvp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(default=140092908100304, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]