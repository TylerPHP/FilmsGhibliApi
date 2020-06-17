from django.contrib import admin

# Register your models here.
from StudioGhibliApi.models import Locate


class LocateAdmin(admin.ModelAdmin):
    """Комната чата"""
    list_display = ("title", "director", "produser")


admin.site.register(Locate, LocateAdmin)
