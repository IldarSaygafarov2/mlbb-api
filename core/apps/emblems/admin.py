from django.contrib import admin

from .models import Emblem


@admin.register(Emblem)
class EmblemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "emblem_type"]
    list_display_links = ["name"]
    list_filter = ["emblem_type"]
