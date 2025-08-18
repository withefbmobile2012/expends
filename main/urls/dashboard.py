from django.urls import path
import main.views.dashboard as view

urlpatterns = [
    path('', view.dashboard, name='dashboard')
]