# Generated by Django 2.2.6 on 2019-10-09 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20191008_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='cover_latter',
            new_name='cover_letter',
        ),
    ]
