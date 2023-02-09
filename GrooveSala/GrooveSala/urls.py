from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from GrooveSala.settings import MEDIA_ROOT, MEDIA_URL
from GrooveSala.views import index, creator

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', creator, name='creator'),

    path('users/', include('users.urls')),

    path('bands/', include('bands.urls')),
    path('turns/', include('bands.urls')),
    path('beverages/', include('beverages.urls')),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
