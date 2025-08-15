from django.urls import path
import main.views.users as views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.register_user, name='register'),
    path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]