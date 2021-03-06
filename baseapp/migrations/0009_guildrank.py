# Generated by Django 4.0 on 2021-12-29 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0008_alter_user_user_guild'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild_rank_name', models.CharField(blank=True, max_length=50, null=True)),
                ('guild_rank_points', models.IntegerField(blank=True, default=0, null=True)),
                ('guild_rank_belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseapp.guild')),
            ],
        ),
    ]
