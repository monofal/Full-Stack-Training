# Generated by Django 2.2.6 on 2019-10-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20191008_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
