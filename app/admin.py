from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Medicine)
admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(Payments)
admin.site.register(Contact)
admin.site.register(Supplier)
admin.site.register(Cart)
# admin.site.register(Prescription)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['Photo']

