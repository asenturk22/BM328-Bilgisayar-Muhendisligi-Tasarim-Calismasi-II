# Generated by Django 4.2 on 2023-05-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_phone_number1_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
    ]
