# Generated by Django 3.1.6 on 2021-06-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0019_destination_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
    ]
