# Generated by Django 3.1.6 on 2021-02-18 09:56

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_remove_incidences_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidences',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
