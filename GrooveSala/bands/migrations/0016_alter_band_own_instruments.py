# Generated by Django 4.1.5 on 2023-02-08 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0015_alter_band_own_instruments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='own_instruments',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
