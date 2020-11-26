from django.test import TestCase
from catalogo.models import Producto

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Producto.objects.create(id='2', nombre='air max 90', precio='90.000', descripcion='zapatilla comoda')
    
    def test_nombre_label(self):
        producto=Producto.objects.get(id=2)
        field_label = producto._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_precio_label(self):
        producto=Producto.objects.get(id=2)
        field_label = producto._meta.get_field('precio').verbose_name
        self.assertEquals(field_label,'precio')
    
    def test_nombre_max_length(self):
        producto=Producto.objects.get(id=2)
        max_length = producto._meta.get_field('nombre').max_length
        self.assertEquals(max_length,20)
    
    def test_descripcion_max_length(self):
        producto=Producto.objects.get(id=2)
        max_length = producto._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,1000)
        
    def test_get_absolute_url(self):
        producto=Producto.objects.get(id=2)
        self.assertEquals(producto.get_absolute_url(), '/catalogo/gg/2')