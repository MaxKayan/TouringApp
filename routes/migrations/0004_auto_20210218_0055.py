# Generated by Django 3.1.6 on 2021-02-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_auto_20210218_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'verbose_name': 'Пункт назначения', 'verbose_name_plural': 'Пункты назначения'},
        ),
        migrations.AlterModelOptions(
            name='destinationphoto',
            options={'verbose_name': 'Фотография точки', 'verbose_name_plural': 'Фотографии точек'},
        ),
        migrations.AlterModelOptions(
            name='waypoint',
            options={'verbose_name': 'Путевая точка', 'verbose_name_plural': 'Путевые точки'},
        ),
        migrations.AddConstraint(
            model_name='waypoint',
            constraint=models.UniqueConstraint(fields=('route', 'longitude', 'latitude'), name='unique_waypoint'),
        ),
    ]
