from django.urls import path

from bands.views import create_band, search_band, update_band, \
                        BandListView, BandDeleteView, \
                            create_turn,\
                            TurnListView

urlpatterns = [
    path('create-band/', create_band, name='create-band'),
    path('bands-list/', BandListView.as_view(), name='bands-list'),
    path('search-band/', search_band, name='search-band'),
    path('delete-band/<int:pk>/', BandDeleteView.as_view(), name='delete-band'),
    path('update-band/<int:id>/', update_band, name='update-band'),

    path('create-turn/', create_turn, name='create-turn'),
    path('turns-list/', TurnListView.as_view(), name='turns-list')
    ]