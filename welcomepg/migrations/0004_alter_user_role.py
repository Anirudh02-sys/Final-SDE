# Generated by Django 4.1.2 on 2022-11-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcomepg', '0003_rename_acts_act_auditor_subcontractor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Auditor', 'Auditor'), ('Subcontractor', 'Subcontractor')], default='Admin', max_length=50, null=True),
        ),
    ]
