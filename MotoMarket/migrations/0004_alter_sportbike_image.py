# Generated by Django 3.2.4 on 2021-06-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoMarket', '0003_sportbike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportbike',
            name='image',
            field=models.ImageField(upload_to='templtes/images'),
        ),
    ]