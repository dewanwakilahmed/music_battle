# Generated by Django 4.0 on 2022-01-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0028_battle_ticket_buyin_user_user_buy_ins_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='sell_back_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
