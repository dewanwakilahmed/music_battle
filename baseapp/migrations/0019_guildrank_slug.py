# Generated by Django 4.0 on 2021-12-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0018_rename_rank_max_points_rank_rank_max_point_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildrank',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
