from django.contrib import admin

from .models import Equipment, EquipmentType, EquipmentStata


class EquipmentStataInline(admin.StackedInline):
    model = EquipmentStata
    extra = 1


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name']
    list_filter = ['equipment_type']
    search_fields = ['name']
    inlines = [
        EquipmentStataInline
    ]
