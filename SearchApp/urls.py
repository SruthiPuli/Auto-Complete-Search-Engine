from django.urls import path 
from . import views
from .backend.triestructure import Trie

urlpatterns = [

    path('', views.home, name = 'home'),
    path('fetchdata/', views.fetch_data, name = 'fetchdata'),
]