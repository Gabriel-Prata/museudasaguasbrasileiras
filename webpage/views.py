from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import GalleryAcervo, GalleryAguasMarginais, GalleryPantanalBrasileiro

# Create your views here.


def home(request):
    context = {
      'current_page': 'home'
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
      'current_page': 'about'
    }
    return render(request, 'pages/about.html', context)


def network(request):
    context = {
      'current_page': 'network'
    }
    return render(request, 'pages/network.html', context)


def galleries(request):
  context = {
    'current_page': 'galleries'
  }
  return render(request, 'pages/galleries.html', context)


def partners(request):
  context = {
    'current_page': 'partners'
  }
  return render(request, 'pages/partners.html', context)


def contact(request):
  context = {
    'current_page': 'contact'
  }
  return render(request, 'pages/contact.html', context)


def news(request):
  context = {
    'current_page': 'news'
  }
  return render(request, 'pages/news.html', context)

def activities(request):
  context = {
    'current_page': 'activities'
  }
  return render(request, 'pages/activities.html', context)

#News:

def news01(request):
   context = {
      'current_page': 'news'
   }
   return render(request, 'pages/news/01aaguaquequeremos.html', context)


#Activities:

def activitieAAguaQueQueremos2024(request):
   context = {
      'current_page': 'activities'
   }
   return render(request, 'pages/activities/aaguaquequeremos2024.html', context)


def activitieMaosQueCuidam(request):
   context = {
      'current_page': 'activities'
   }
   return render(request, 'pages/activities/maosquecuidam.html', context)



#Galleries:

def galleryAAguaQueQueremos(request):
   context = {
      'current_page': 'galleries'
   }
   return render(request, 'pages/galleries/aaguaquequeremos.html', context)


def galleryOCurupira(request):
  context = {
    'current_page': 'galleries'
  }
  return render(request, 'pages/galleries/ocurupira.html', context)  



def galleryCustos(request):
  context = {
    'current_page': 'galleries'
  }
  return render(request, 'pages/galleries/custos.html', context)  



def galleryAguasMarginais(request):
  images = GalleryAguasMarginais.objects.all()
  context = {
     'images': images,
     'current_page': 'galleries'
  }
  return render(request, 'pages/galleries/aguasmarginais.html', context)


def galleryPantanalBrasileiro(request):
  images = GalleryPantanalBrasileiro.objects.all()
  context = {
     'images': images,
     'current_page': 'galleries'
  }
  return render(request, 'pages/galleries/pantanalbrasileiro.html', context)


def galleryAcervo(request):
  images = GalleryAcervo.objects.all()
  context = {
     'images': images,
     'current_page': 'galleries'
  }
  return render(request, 'pages/galleries/acervo.html', context)
