# Generated by Django 4.1.5 on 2023-02-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverages', '0002_beverage_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='brand',
            field=models.CharField(max_length=50),
        ),
    ]