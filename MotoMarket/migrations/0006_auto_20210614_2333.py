# Generated by Django 3.2.4 on 2021-06-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoMarket', '0005_alter_sportbike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportbike',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='sportbike',
            name='image',
            field=models.ImageField(upload_to='MotoMarket/templates/images'),
        ),
    ]