from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='home'),
    path('new', views.new, name='page_1'),
    path('contacts', views.contacts, name='last'),
    path('user', views.user, name='page_2')
]