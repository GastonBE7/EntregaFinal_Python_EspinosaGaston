from django.urls import path

from beverages.views import create_beverage, search_beverages, \
                        BeveragesListView

urlpatterns = [
    path('create-beverage/', create_beverage, name='create-beverage'),
    path('beverages-list/', BeveragesListView.as_view(), name='beverages-list'),
    path('search-beverages/', search_beverages, name='search_beverages'),
    ]