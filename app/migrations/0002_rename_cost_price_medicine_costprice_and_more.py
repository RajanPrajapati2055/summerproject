# Generated by Django 4.0.5 on 2022-06-09 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='Cost_price',
            new_name='costprice',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='Medicine_CompanyName',
            new_name='medicinecompanyname',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='Medicine_Name',
            new_name='medicinename',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='Selling_price',
            new_name='sellingprice',
        ),
    ]
