# Generated by Django 2.1.5 on 2023-03-12 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicial', '0012_auto_20230312_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 12, 17, 7, 55, 944113)),
        ),
    ]
