# Generated by Django 4.1.2 on 2023-04-23 11:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('osm_id', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=28, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'Amenities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('osm_id', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=28, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('ward', models.IntegerField(blank=True, null=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=10, null=True)),
                ('housemetricnumber', models.CharField(blank=True, max_length=50, null=True)),
                ('people', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Buildings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('osm_id', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=28, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'Forest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('osm_id', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=28, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('ref', models.CharField(blank=True, max_length=20, null=True)),
                ('oneway', models.CharField(blank=True, max_length=1, null=True)),
                ('maxspeed', models.SmallIntegerField(blank=True, null=True)),
                ('layer', models.FloatField(blank=True, null=True)),
                ('bridge', models.CharField(blank=True, max_length=1, null=True)),
                ('tunnel', models.CharField(blank=True, max_length=1, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'Road',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waterbody',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('osm_id', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.SmallIntegerField(blank=True, null=True)),
                ('fclass', models.CharField(blank=True, max_length=28, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'Waterbody',
                'managed': False,
            },
        ),
    ]
