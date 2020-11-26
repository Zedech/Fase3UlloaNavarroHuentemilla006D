from django.db import models
from django.urls import reverse  #direcciona a una url de un producto al browser
import uuid  #se utiliza para definir atributos claves o la PK

# Create your models here.

class Marca(models.Model):
        marca = models.CharField(max_length=100, help_text='Ingrese la marca y el tipo de producto EJ: Nike, Zapatilla; adidas, poleron')
		
        
    
        def __str__(self):
	        return self.marca

			

class Producto(models.Model):
	id=models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	precio=models.CharField(max_length=50)
	descripcion = models.TextField(max_length=1000, help_text='Ingrese una descripcion')
	marca=models.ManyToManyField(Marca)	
	
	
	def __str__(self):
		return f'{self.nombre}, {self.descripcion}'
	
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('producto-detalles', args=[str(self.id)])
			
