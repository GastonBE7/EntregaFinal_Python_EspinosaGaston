# Generated by Django 4.1.5 on 2023-02-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0014_remove_turn_own_instruments_band_own_instruments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='own_instruments',
            field=models.BooleanField(),
        ),
    ]
