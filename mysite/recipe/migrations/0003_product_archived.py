# Generated by Django 5.1.4 on 2025-01-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_product_created_at_product_discount_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
