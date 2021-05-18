from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Tipo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Receta(models.Model):
    
	titulo = models.CharField(max_length=200)
	imagen = models.ImageField(null=True, blank=True)
	ingredientes = models.TextField(max_length=300)
	tipo = models.ManyToManyField(Tipo)
	descripcion = models.TextField(max_length=1000)
		  
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this manga."""
		return reverse('receta-detail', args=[str(self.id)])

