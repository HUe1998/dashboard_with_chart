from django.urls import path
from django.urls import path
from .views import dashboardView

urlpatterns = [
    path('dashboard/', dashboardView, name='dashboard'),
]
