# Generated by Django 4.0 on 2022-01-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0026_alter_user_user_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseapp.rank'),
        ),
    ]
