from django.contrib import admin

from .models import HeroSpecialty


@admin.register(HeroSpecialty)
class HeroSpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name", "description")
    ordering = ("-created_at",)
