# Generated by Django 3.1.5 on 2021-07-30 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0026_company_director_yata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_bank',
            new_name='company_funds',
        ),
    ]
