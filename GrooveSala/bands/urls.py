from django.urls import path

from bands.views import create_band, search_band, update_band, \
                        BandListView, BandDeleteView, EventListView, EventDeleteView, \
                            create_turn, first_time, create_first_turn, my_turns, create_event, \
                            TurnListView, TurnDeleteView

urlpatterns = [
    path('create-band/', create_band, name='create-band'),
    path('bands-list/', BandListView.as_view(), name='bands-list'),
    path('search-band/', search_band, name='search-band'),
    path('delete-band/<int:pk>/', BandDeleteView.as_view(), name='delete-band'),
    path('update-band/<int:id>/', update_band, name='update-band'),

    path('create-event/', create_event, name='create-event'),
    path('events-list/', EventListView.as_view(), name='events-list'),
    path('cancel-event/<int:pk>/', EventDeleteView.as_view(), name='cancel-event'),

    path('first-time/', first_time ,name='first-time'),
    path('create-first-turn/', create_first_turn, name='create-first-turn'),
    path('create-turn/', create_turn, name='create-turn'),
    path('turns-list/', TurnListView.as_view(), name='turns-list'),
    path('cancel-turn/<int:pk>/', TurnDeleteView.as_view(), name='cancel-turn'),
    path('my-turns/', my_turns, name='my-turns')
    ]