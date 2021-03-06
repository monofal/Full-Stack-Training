# Generated by Django 2.2.6 on 2019-10-04 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20191003_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='employee_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.EmployeeProfile'),
            preserve_default=False,
        ),
    ]
