from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="home"),
    path("About/",views.About, name = "About"),
    path("Login/",views.loginPage, name = "login"),
    path('signout/', views.signout, name="User Sign Out"),
    path("Register/",views.Register, name = "Register"),
    path("Contact/",views.contact, name = "Contact"),
    path("Medicine/",views.medicine, name = "Medicine"),
    path("Supplier/",views.supplier, name = "Supplier"),
    path("Dashboard/",views.Dashboard, name = "Dashboard"),
    path("cart/",views.cart, name = "cart"),
    path("supplierdata/",views.supplierdata, name = "supplierdata"),
    path("Product/",views.Product, name = "Product"),
    path("customerdetail/",views.customerdetail, name = "customerdetail"),




    

    
] 