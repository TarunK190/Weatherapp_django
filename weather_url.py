from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather, name='weather'),
]
Include the app’s URLs in your project’s urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),
]