# Generated by Django 3.2.4 on 2021-06-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
