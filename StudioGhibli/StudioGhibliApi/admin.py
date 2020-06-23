from django.contrib import admin

# Register your models here.
from .models import Category, Locate


class CategoryAdmin(admin.ModelAdmin):
    """Предстваление category"""
    list_display = ('category',)


class LocateAdmin(admin.ModelAdmin):
    """Представление locate"""
    list_display = ('id_category', 'ru_locate', 'us_locate')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Locate, LocateAdmin)
