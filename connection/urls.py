from django.urls import path

from . import views

app_name = 'connection'
urlpatterns = [
    path('', views.index, name='index'),
]
