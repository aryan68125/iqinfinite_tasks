# Generated by Django 5.0.5 on 2024-05-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0004_userprofile_created_at_userprofile_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_blocked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
