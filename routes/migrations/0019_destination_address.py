# Generated by Django 3.1.6 on 2021-04-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0018_route_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Адрес'),
        ),
    ]