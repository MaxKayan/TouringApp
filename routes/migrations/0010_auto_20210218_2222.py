# Generated by Django 3.1.6 on 2021-02-18 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0009_destination_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='routes.route', verbose_name='Маршрут'),
        ),
    ]