from django.contrib import admin

# Register your models here.
from . models import Tipo, Receta

admin.site.register(Tipo)
admin.site.register(Receta)