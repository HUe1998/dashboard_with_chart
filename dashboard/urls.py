from django.urls import path
from django.urls import path, include
from .views import dashboardView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', dashboardView, name='dashboard'),
]
