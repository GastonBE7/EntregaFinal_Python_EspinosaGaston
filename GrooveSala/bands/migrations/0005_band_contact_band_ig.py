# Generated by Django 4.1.5 on 2023-01-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_remove_band_contact_remove_band_ig'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='contact',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='ig',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
