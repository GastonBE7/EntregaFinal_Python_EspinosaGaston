from django.urls import path

from bands.views import create_band, search_band, update_band, \
                        BandListView, BandDeleteView

urlpatterns = [
    path('create-band/', create_band, name='create-band'),
    path('bands-list/', BandListView.as_view(), name='bands-list'),
    path('search-band/', search_band, name='search-band'),
    path('delete-band/<int:pk>/', BandDeleteView.as_view(), name='delete-band'),
    path('update-band/<int:id>/', update_band, name='update-band'),
]