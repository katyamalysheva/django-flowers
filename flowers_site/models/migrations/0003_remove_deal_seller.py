# Generated by Django 4.0.4 on 2022-08-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_lot_flower_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='seller',
        ),
    ]
