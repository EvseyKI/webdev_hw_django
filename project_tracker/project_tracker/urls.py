from django.contrib import admin
from django.urls import path, include
from project_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('tasks/', include('tasks.urls')),
    path('quality-control/', include('quality_control.urls')),
]
