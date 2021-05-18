from django.db import models
from django.urls import reverse
import uuid

class Tipo(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


class Receta(models.Model):

    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)
    ingredientes = models.TextField(max_length=300)
    tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True, blank=False)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this manga."""
        return reverse('receta_detail', args=[str(self.id)])
