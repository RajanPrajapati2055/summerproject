# Generated by Django 4.0.5 on 2022-07-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DoctorName', models.CharField(max_length=100)),
                ('HospitalName', models.EmailField(max_length=254)),
                ('HospitalContact', models.BigIntegerField()),
                ('HospitalAddress', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]