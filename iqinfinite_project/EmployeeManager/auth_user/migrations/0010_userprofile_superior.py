# Generated by Django 5.0.5 on 2024-05-31 12:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0009_rename_is_blocked_userprofile_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='superior',
            field=models.ForeignKey(default=29, on_delete=django.db.models.deletion.CASCADE, related_name='superior_officer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
