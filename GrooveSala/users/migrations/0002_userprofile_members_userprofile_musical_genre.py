# Generated by Django 4.1.5 on 2023-02-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='members',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='musical_genre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
