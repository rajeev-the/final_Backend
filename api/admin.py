# admin.py
from django.contrib import admin
from .models import Agent, Property, GeneralData,UserData

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'estate_name', 'phone_number', 'rating', 'verifications')
    search_fields = ('name', 'estate_name')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'district_name',
        'tehsil_name',
        'village_name',
        'acre',
        'acre_price',
        'money_unit',
        'unit_of_land',
        'available',
        'isvaild',
        'sale_or_lease',
        'agent',
    )
    search_fields = (
        'address',
        'district_name',
        'tehsil_name',
        'village_name',

    )
    list_filter = (
        'available',
        'isvaild',
        'land_category',
        'sale_or_lease',
        'money_unit',
        'unit_of_land',
        'district_name',
        'agent',
    )


@admin.register(GeneralData)
class GeneralDataAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('top_rate', 'featured', 'recommendation')

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')  # Allow searching by name & phone