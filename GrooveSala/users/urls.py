from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register, update_user_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('signup/', register, name='register'),

    path('update-profile/', update_user_profile, name='update-profile'),
]