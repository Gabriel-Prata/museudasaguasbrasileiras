from django.urls import path
from . import views

app_name = 'webpage'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('network/', views.network, name='network'),
    path('galleries/', views.galleries, name='galleries'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('activities/', views.activities, name='activities'),
]