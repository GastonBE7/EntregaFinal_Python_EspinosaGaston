from django.urls import path

from bands.views import create_band, \
                        BandListView, BandDeleteView

urlpatterns = [
    path('create-band/', create_band, name='create-band'),
    path('bands-list/', BandListView.as_view(), name='bands-list'),
    path('delete-band/<int:pk>/', BandDeleteView.as_view(), name='delete-band')
]