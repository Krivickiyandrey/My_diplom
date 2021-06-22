# Generated by Django 3.2.4 on 2021-06-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoMarket', '0007_auto_20210615_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='korzina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('motomodel', models.CharField(max_length=255)),
                ('engine', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
            ],
        ),
    ]
