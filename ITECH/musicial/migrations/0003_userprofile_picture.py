# Generated by Django 2.1.5 on 2023-02-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicial', '0002_remove_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=1, upload_to='profile_images'),
            preserve_default=False,
        ),
    ]
