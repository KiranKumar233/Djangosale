from django.contrib import admin

# Register your models here.
# your_app/admin.py
from .models import NewPropertyData

class NewPropertyDataAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'property_type', 'status_name', 'property_cost', 'property_size', 'seller_contact_details')
    search_fields = ['property_name', 'property_type', 'status_name', 'seller_contact_details']
    list_filter = ('property_type', 'status_name')

admin.site.register(NewPropertyData, NewPropertyDataAdmin)
