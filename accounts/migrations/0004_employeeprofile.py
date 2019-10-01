# Generated by Django 3.1 on 2019-09-30 13:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190927_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(error_messages={'required': 'First name must be provided'}, max_length=50)),
                ('last_name', models.CharField(error_messages={'required': 'Last name must be provided'}, max_length=50)),
                ('years_of_experience', models.FloatField(error_messages={'required': 'Years of experience must be provided'}, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('image_path', models.CharField(max_length=500, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
            options={
                'db_table': 'employee_profile',
            },
        ),
    ]
