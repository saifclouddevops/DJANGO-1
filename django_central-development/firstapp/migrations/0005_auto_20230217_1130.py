# Generated by Django 3.2 on 2023-02-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20230217_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='app_belongs',
            field=models.CharField(choices=[(0, 'Select Belongs'), ('mcs', 'MCS'), ('ajax', 'Ajax'), ('vvgroups', 'VVGroups')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='based_on',
            field=models.CharField(choices=[(0, 'Select APP'), ('odoo', 'Odoo'), ('elasticsearch', 'Elastic Search')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='server_selection',
            field=models.CharField(choices=[(0, 'Select Server'), ('live', 'Live'), ('local', 'Local')], default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='server_status_on',
            field=models.CharField(choices=[(0, 'Select Status'), ('live', 'Live'), ('testing', 'Testing'), ('alpha', 'Alpha'), ('beta', 'Beta')], default=0, max_length=20, null=True),
        ),
    ]
