# Generated by Django 3.1.7 on 2021-04-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0021_auto_20210430_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='metEntrega',
            field=models.TextField(max_length=50, null=True),
        ),
    ]