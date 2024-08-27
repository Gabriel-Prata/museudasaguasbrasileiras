from django.contrib import admin

# Register your models here.
from .models import GalleryAcervo, GalleryAguasMarginais, GalleryPantanalBrasileiro


admin.site.register(GalleryAcervo)

admin.site.register(GalleryAguasMarginais)

admin.site.register(GalleryPantanalBrasileiro)

