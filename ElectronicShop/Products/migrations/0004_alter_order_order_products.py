# Generated by Django 4.1.5 on 2023-03-20 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_order_quentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_Products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Products.products'),
        ),
    ]
