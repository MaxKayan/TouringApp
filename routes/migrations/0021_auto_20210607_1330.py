# Generated by Django 3.1.6 on 2021-06-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0020_destination_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='short_description',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Краткое описание'),
        ),
    ]