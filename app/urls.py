from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="home"),
    path("About/",views.About, name = "About"),
    path("Login/",views.loginPage, name = "login"),
    path('signout/', views.signout, name="User Sign Out"),
    path("Register/",views.Register, name = "Register"),
    path("Contact/",views.contact, name = "Contact"),
    path("Feedback/",views.feedback, name = "Feedback"),
    path("order/",views.Order, name = "order"),
    path("Medicine/",views.medicine, name = "Medicine"),
    path("Supplier/",views.supplier, name = "Supplier"),
    path("Dashboard/",views.Dashboard, name = "Dashboard"),
    path("addtocart/<int:id>/",views.add_to_cart, name = "cart"),
    path('cartshow/', views.show_cart, name='showcart'),
    path("removecart/<int:id>/", views.remove_cart, name='remove_cart'),
    path("supplierdata/",views.supplierdata, name = "supplierdata"),
    path('deletesupplier/<int:id>/',views.delete_supplier, name = "deletesupplier"),
    path("supplierupdate/<int:id>/",views.update_supplier, name = "supplierupdate"),
    path("Product/",views.Product, name = "Product"),
    path('delete/<int:id>/',views.delete_medicine, name = "deletemedicine"),
    path("medicineupdate/<int:id>/",views.updatemedicine, name = "medicineupdate"),
    path("customerdetail/",views.customerdetail, name = "customerdetail"),
    path("payment/",views.Payment, name = "payment"),
    path("prescription/",views.prescriptions, name = "prescription"),
    path("khaltirequest/",views.Khaltirequest, name = "khaltirequest"),
    

    
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

