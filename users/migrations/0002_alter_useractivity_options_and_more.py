# Generated by Django 5.1.3 on 2024-12-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useractivity',
            options={'verbose_name': 'UserActivity', 'verbose_name_plural': 'UserActivities'},
        ),
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name': 'UserSetting', 'verbose_name_plural': 'UserSettings'},
        ),
        migrations.AddField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]