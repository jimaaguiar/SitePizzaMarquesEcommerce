# Generated by Django 3.1.7 on 2021-04-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0013_auto_20210428_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telemovel',
            field=models.IntegerField(null=True),
        ),
    ]
