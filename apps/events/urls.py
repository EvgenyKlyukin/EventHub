from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('test/', views.homepage, name='homepage'),
]
