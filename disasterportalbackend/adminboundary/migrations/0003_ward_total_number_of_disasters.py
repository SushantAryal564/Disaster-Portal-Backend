# Generated by Django 4.1.2 on 2023-02-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminboundary', '0002_ward_number_of_disasters'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='total_number_of_disasters',
            field=models.PositiveIntegerField(default=0),
        ),
    ]