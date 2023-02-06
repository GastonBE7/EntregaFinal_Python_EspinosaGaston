from django.contrib import admin
from django.urls import path, include

from GrooveSala.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('bands/', include('bands.urls')),
    path('turns/', include('bands.urls')),
    path('beverages/', include('beverages.urls')),
]
