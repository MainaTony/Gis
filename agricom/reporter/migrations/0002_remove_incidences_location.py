# Generated by Django 3.1.6 on 2021-02-18 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidences',
            name='location',
        ),
    ]
