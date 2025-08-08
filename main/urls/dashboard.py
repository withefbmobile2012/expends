from django.urls import path
from main.views import dashboard as views


urlpatterns = [
    path('', views.filtering_daily, name='filtering_daily'),
    path('create/', views.filtering_weekly, name='filtering_weekly'),
    path('<int:pk>/update/', views.filtering_monthly, name='filtering_monthly'),
    path('<int:pk>/delete/', views.filtering_by_categories, name='filtering_by_categories'),
]
