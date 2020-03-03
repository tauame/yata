# Generated by Django 3.0.1 on 2020-03-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0036_remove_player_apikey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='section',
            field=models.CharField(choices=[('B', 'bazaar'), ('F', 'faction'), ('T', 'target'), ('A', 'awards'), ('S', 'stock'), ('L', 'loot')], default='B', max_length=16),
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]