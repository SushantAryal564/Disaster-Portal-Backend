# Generated by Django 4.1.2 on 2023-04-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasterevent',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]