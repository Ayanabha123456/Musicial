# Generated by Django 2.1.5 on 2023-03-04 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicial', '0008_auto_20230304_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendprofile',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friendprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_user', to='musicial.UserProfile'),
        ),
    ]
