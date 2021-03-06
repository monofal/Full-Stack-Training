# Generated by Django 2.2.6 on 2019-10-02 07:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191001_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('document_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('document_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='years_of_experience',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(error_messages={'required': 'Institute name must be provided'}, max_length=255)),
                ('degree', models.CharField(error_messages={'required': 'Degree must be provided'}, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('percentage_marks', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('cgpa', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
            options={
                'db_table': 'qualification',
            },
        ),
        migrations.CreateModel(
            name='EmployeeSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.EmployeeProfile')),
                ('skill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Skill')),
            ],
            options={
                'db_table': 'employee_skills',
            },
        ),
    ]
