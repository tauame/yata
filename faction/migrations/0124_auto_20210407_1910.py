# Generated by Django 3.1.5 on 2021-04-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0123_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction', models.IntegerField(db_index=True, default=0)),
                ('target_id', models.IntegerField(db_index=True, default=0)),
                ('strength', models.BigIntegerField(default=0)),
                ('speed', models.BigIntegerField(default=0)),
                ('defense', models.BigIntegerField(default=0)),
                ('dexterity', models.BigIntegerField(default=0)),
                ('total', models.BigIntegerField(default=0)),
                ('strength_timestamp', models.IntegerField(default=0)),
                ('speed_timestamp', models.IntegerField(default=0)),
                ('defense_timestamp', models.IntegerField(default=0)),
                ('dexterity_timestamp', models.IntegerField(default=0)),
                ('total_timestamp', models.IntegerField(default=0)),
                ('target_name', models.CharField(default='Player', max_length=32)),
                ('target_faction_name', models.CharField(default='Faction', max_length=64)),
                ('target_faction_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='faction',
            name='armoryNewsFilter',
        ),
        migrations.RemoveField(
            model_name='faction',
            name='armoryUpda',
        ),
        migrations.AddField(
            model_name='faction',
            name='factions_spies',
            field=models.TextField(default='[]'),
        ),
    ]