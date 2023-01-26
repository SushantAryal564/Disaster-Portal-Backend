# Generated by Django 4.1.2 on 2023-01-26 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasterevent',
            name='is_closed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disasterevent',
            name='is_verified',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='disasterevent',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterApp.rating'),
        ),
        migrations.AlterField(
            model_name='disasterevent',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='disasterApp.disastertype'),
        ),
    ]