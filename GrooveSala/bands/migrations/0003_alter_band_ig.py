# Generated by Django 4.1.5 on 2023-01-29 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_band_contact_band_ig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='ig',
            field=models.CharField(default=True, max_length=100),
        ),
    ]