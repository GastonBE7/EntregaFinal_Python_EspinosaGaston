# Generated by Django 4.1.5 on 2023-02-08 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userprofile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='members',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='musical_genre',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]