from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'connection'
urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('name/create/', views.NameCreate.as_view(), name='name-create'),
    path('name/<int:pk>/update/',
         views.NameUpdate.as_view(), name='name-update'),
    path('name/<int:pk>/delete/',
         views.NameDelete.as_view(), name='name-delete'),
    path('name/<int:pk>/', views.NameDetailView.as_view(), name='name-detail'),
    path('name/', views.NameListView.as_view(), name='name'),
    path('contact/', views.contact_form, name="connection-contact"),

    path('country/',
         cache_page(10)(views.CountryCityList.as_view()), name='country')
]
