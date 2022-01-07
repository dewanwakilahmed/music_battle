# Generated by Django 4.0 on 2022-01-06 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0022_user_user_is_profile_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(blank=True, max_length=255, null=True)),
                ('genre_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('genre_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.genre'),
        ),
    ]
