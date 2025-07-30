from django.urls import path
from main.views import category as views


urlpatterns = [
    path('', views.category_read, name='category_list'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/update/', views.category_update, name='category_update'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
]
