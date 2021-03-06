# Generated by Django 3.1.6 on 2021-02-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0006_auto_20210218_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота'),
        ),
    ]
