# Generated by Django 4.0.5 on 2022-06-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_cost_price_medicine_costprice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='Supplierontact',
            new_name='Suppliercontact',
        ),
    ]