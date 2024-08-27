from django.db import models

# Create your models here.

class GalleryAguasMarginais(models.Model):
  image = models.ImageField(upload_to='media/galleries/aguasmarginais')
  title = models.CharField(max_length=600)

  def __str__(self) -> str:
    return self.title
  

class GalleryPantanalBrasileiro(models.Model):
  image = models.ImageField(upload_to='media/galleries/pantanal')
  title = models.CharField(max_length=600)

  def __str__(self) -> str:
    return self.title
  

class GalleryAcervo(models.Model):
  image = models.ImageField(upload_to='media/galleries/acervo')
  title = models.CharField(max_length=600)

  def __str__(self) -> str:
    return self.title
  
