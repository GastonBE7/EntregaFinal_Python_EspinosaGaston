from django.contrib import admin

from bands.models import Band

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name_band', 'musical_genre', 'own_instruments', 'contact')
    list_filter = ('own_instruments',)
    search_fields = ('name_band',)
