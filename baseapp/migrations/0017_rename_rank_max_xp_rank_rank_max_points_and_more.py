# Generated by Django 4.0 on 2021-12-30 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0016_rename_rank_max_point_rank_rank_max_xp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rank',
            old_name='rank_max_xp',
            new_name='rank_max_points',
        ),
        migrations.RenameField(
            model_name='rank',
            old_name='rank_min_xp',
            new_name='rank_min_points',
        ),
    ]