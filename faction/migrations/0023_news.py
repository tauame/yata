# Generated by Django 3.0.1 on 2020-02-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0022_faction_chainsupda'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='typenews', max_length=16)),
                ('tId', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(default=0)),
                ('news', models.CharField(default='news', max_length=128)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faction.Faction')),
            ],
        ),
    ]