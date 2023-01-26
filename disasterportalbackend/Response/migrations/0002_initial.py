# Generated by Django 4.1.2 on 2023-01-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Response', '0001_initial'),
        ('adminboundary', '0002_lalitpurmetro'),
        ('disasterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wardresponseteams',
            name='disaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterApp.disasterevent'),
        ),
        migrations.AddField(
            model_name='wardresponseteammembers',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Response.wardresponseteams'),
        ),
        migrations.AddField(
            model_name='wardresponseteammembers',
            name='volunters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Response.volunters'),
        ),
        migrations.AddField(
            model_name='muniresponseteams',
            name='disaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterApp.disasterevent'),
        ),
        migrations.AddField(
            model_name='muniresponseteammembers',
            name='municipal_police',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Response.municipalpolice'),
        ),
        migrations.AddField(
            model_name='muniresponseteammembers',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Response.wardresponseteams'),
        ),
        migrations.AddField(
            model_name='muniresponseteammembers',
            name='volunters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Response.volunters'),
        ),
        migrations.AddField(
            model_name='inventoryward',
            name='Ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminboundary.ward'),
        ),
        migrations.AddField(
            model_name='inventoryward',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Response.inventorylist'),
        ),
        migrations.AddField(
            model_name='inventorymunicipality',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Response.inventorylist'),
        ),
        migrations.AddField(
            model_name='inventorylist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Response.inventorycategory'),
        ),
        migrations.AddField(
            model_name='activitylog',
            name='disaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disasterApp.disasterevent'),
        ),
    ]
