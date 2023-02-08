from django.contrib import admin

from bands.models import Band, Turn

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name_band', 'musical_genre', 'contact',)
    list_filter = ('musical_genre',)
    search_fields = ('name_band',)

@admin.register(Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('name_band', 'turn_assigned', 'own_instruments',)
