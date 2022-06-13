from django.db import models
# from models import Medicine
# from django.contrib.auth.models import User



# Create your models here.
class Admin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)


class Medicine(models.Model):
    medicinename = models.CharField(max_length=100)
    costprice = models.FloatField(max_length=100)
    sellingprice = models.FloatField(max_length=100)
    medicinecompanyname = models.CharField(max_length=100)
    #Order = models.ForeignKey(Order,blank=True, null=True)
    #Stock = models.TextField(blank=True, null=True)
    def __str__(self):
     return str(self.medicinename)
    

class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
     return str(self.fullname)


# class Order(models.Model):
#     email = models.TextField(blank=True, null=True)
#     password = models.TextField(blank=True, null=True)
#     username = models.TextField(blank=True, null=True)
#     Customer = models.ForeignKey(Customer,blank=True, null=True)
#     quantity = models.FloatField(blank=True, null=True)

    
# class Payments(models.Model):
#     amount = models.FloatField(blank=True, null=True)
#     paiddate = models.DateTimeField(default="null")
#   #  Order = models.ForeignKey(Order,blank=True, null=True)

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    phone=models.BigIntegerField()
    desc=models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
     return str(self.name)


class Supplier(models.Model):
    Suppliername = models.CharField(max_length=100)
    Supplieremail = models.EmailField()
    Supplierontact = models.BigIntegerField()
    Supplieraddress = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Suppliername)



