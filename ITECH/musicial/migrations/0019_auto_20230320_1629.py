# Generated by Django 2.1.5 on 2023-03-20 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicial', '0018_auto_20230318_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 16, 29, 11, 244025)),
        ),
    ]