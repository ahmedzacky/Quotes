# Generated by Django 3.0.3 on 2020-04-05 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='favorite_quote',
        ),
    ]
