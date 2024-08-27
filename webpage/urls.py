from django.urls import path
from . import views

app_name = 'webpage'

urlpatterns = [
  #staticpages
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('network/', views.network, name='network'),
  path('galleries/', views.galleries, name='galleries'),
  path('partners/', views.partners, name='partners'),
  path('contact/', views.contact, name='contact'),
  path('news/', views.news, name='news'),
  path('activities/', views.activities, name='activities'),
  #galerias
  path('galleries/aguasmarginais/', views.galleryAguasMarginais,         name='galleryAguasMarginais'),
  path('galleries/pantanalbrasileiro/', views.galleryPantanalBrasileiro,name='galleryPantanalBrasileiro'),
  path('galleries/aaguaquequeremos2024/', views.galleryAAguaQueQueremos,name='galleryAAguaQueQueremos'),
  path('galleries/ocurupira/', views.galleryOCurupira,name='galleryOCurupira'),
  path('galleries/custos/', views.galleryCustos,name='galleryCustos'),
  path('galleries/acervo/', views.galleryAcervo,name='galleryAcervo'),
  #atividades
  path('activities/aaguaquequeremos2024/', views.activitieAAguaQueQueremos2024,name='activitieAAguaQueQueremos2024'),
  path('activities/maosquecuidamdaagua/', views.activitieMaosQueCuidam,name='activitieMaosQueCuidam'),
  #noticias
  path('news/01202401/',views.news01,name='news01')
]