# Generated by Django 3.2.4 on 2021-06-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoMarket', '0006_auto_20210614_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruiser',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cruiser',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
