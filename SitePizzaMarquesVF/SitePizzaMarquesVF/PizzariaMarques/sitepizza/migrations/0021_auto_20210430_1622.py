# Generated by Django 3.1.7 on 2021-04-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepizza', '0020_auto_20210430_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='andar',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='nrPorta',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='rua',
        ),
        migrations.AddField(
            model_name='checkout',
            name='morada',
            field=models.TextField(max_length=50, null=True),
        ),
    ]