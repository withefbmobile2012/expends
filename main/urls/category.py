from django.urls import path
from main.views import category as views


urlpatterns = [
    path('', views.categories_list, name='category'),
    path('create/', views.category_create, name='category'),
    path('<int:pk>/update/', views.category_update, name='category'),
    path('<int:pk>/delete/', views.category_delete, name='category'),
    path('int:pk/detail/', views.categories_detail, name='category'),
]
