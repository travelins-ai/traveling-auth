# Generated by Django 4.2.5 on 2023-09-24 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
    ]
