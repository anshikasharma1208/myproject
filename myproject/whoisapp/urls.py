from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whois/',views.whois_lookup, name='whois_lookup'),
]
