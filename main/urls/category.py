from django.urls import path
from main.views import category as views


urlpatterns = [
    path('', views.categories_list, name='category_list'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/update/', views.categories_update, name='category_update'),
    path('<int:pk>/delete/', views.categories_delete, name='category_delete'),
    path('int:pk/detail/', views.categories_detail, name='category_detail')
]
