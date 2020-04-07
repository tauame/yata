# Generated by Django 3.0.4 on 2020-04-07 19:28

import bot.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0045_rackets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='racketChannels',
            field=models.CharField(blank=True, default='["territory"]', help_text='Name of the racket channels. Can be multiple channels. It has to be the exact channel name: ["channel-a", "my-other-channel"]', max_length=64, validators=[bot.models.channel_names_reg]),
        ),
        migrations.AlterField(
            model_name='guild',
            name='racketRoles',
            field=models.CharField(blank=True, default='["Territory"]', help_text='Name of the role to mention. It has to be the exact role name: ["Role a"] or empty array [] for no mentions.', max_length=64),
        ),
    ]