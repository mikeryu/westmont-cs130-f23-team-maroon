# Generated by Django 4.2.5 on 2023-12-06 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0023_merge_20231130_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
    ]
