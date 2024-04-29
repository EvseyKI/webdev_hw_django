from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('', include('quality_control.urls')),
]
