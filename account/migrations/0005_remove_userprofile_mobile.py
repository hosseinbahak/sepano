# Generated by Django 4.2 on 2023-04-13 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_userprofile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile',
        ),
    ]
