# Generated by Django 3.1.7 on 2021-04-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0017_auto_20210430_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
