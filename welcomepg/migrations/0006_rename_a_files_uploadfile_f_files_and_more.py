# Generated by Django 4.1.2 on 2022-11-23 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcomepg', '0005_uploadfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfile',
            old_name='a_files',
            new_name='f_files',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='a_name',
        ),
    ]