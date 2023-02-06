from django.contrib import admin

from beverages.models import Beverage

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ('brand', 'size', 'quantity',)
    list_filter = ('size', 'quantity',)
    search_fields = ('brand',)
