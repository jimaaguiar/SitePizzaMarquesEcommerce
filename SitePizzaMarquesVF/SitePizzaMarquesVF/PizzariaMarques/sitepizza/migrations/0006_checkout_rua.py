# Generated by Django 3.1.7 on 2021-04-28 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0005_remove_checkout_rua'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='rua',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
