# Generated by Django 5.0 on 2023-12-23 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='quantity',
        ),
    ]
