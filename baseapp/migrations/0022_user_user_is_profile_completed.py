# Generated by Django 4.0 on 2022-01-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0021_guildrank_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_is_profile_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
