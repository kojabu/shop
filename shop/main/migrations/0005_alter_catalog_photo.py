# Generated by Django 4.2.7 on 2023-11-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_catalog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='photo',
            field=models.ImageField(default='shop/main/templates/main/media/empty.png', upload_to='photo/%Y/%m/%d/', verbose_name='Image of product'),
        ),
    ]