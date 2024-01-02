# Generated by Django 3.2 on 2023-02-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20230217_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='app_belongs',
            field=models.CharField(blank=True, choices=[('', 'Select Belongs'), ('mcs', 'MCS'), ('ajax', 'Ajax'), ('vvgroups', 'VVGroups')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='based_on',
            field=models.CharField(blank=True, choices=[('', 'Select APP'), ('odoo', 'Odoo'), ('elasticsearch', 'Elastic Search')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='server_selection',
            field=models.CharField(blank=True, choices=[('', 'Select Server'), ('live', 'Live'), ('local', 'Local')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='server_status_on',
            field=models.CharField(blank=True, choices=[('', 'Select Status'), ('live', 'Live'), ('testing', 'Testing'), ('alpha', 'Alpha'), ('beta', 'Beta')], default='', max_length=20, null=True),
        ),
    ]