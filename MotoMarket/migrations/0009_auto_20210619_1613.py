# Generated by Django 3.2.4 on 2021-06-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoMarket', '0008_korzina'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduro',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='quadro',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sportbike',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
