# Generated by Django 3.1.7 on 2021-04-28 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0004_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='rua',
        ),
    ]