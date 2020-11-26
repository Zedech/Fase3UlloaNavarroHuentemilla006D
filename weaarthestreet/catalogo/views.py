from django.shortcuts import render
from .models import Producto, Marca
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    
    num_Marca_tipo=Marca.objects.all().count()
    num_Productos=Producto.objects.all().count()
    

    return render(
        request,
        'index.html',
        context={'num_productos': num_Productos, 'num_marca': num_Marca_tipo},
    )
def ropa_hombre(request):
    
    return render(
        request,
        'ropa_hombre.html',
    )

def zapatilla_hombre(request):
    
    return render(
        request,
        'zapatilla_hombre.html',
    )

def zapatilla_mujer(request):
    
    return render(
        request,
        'zapatilla_mujer.html',
    )
def accesorios(request):
    
    return render(
        request,
        'accesorios.html',
    )

def contacto(request):
    
    return render(
        request,
        'contacto.html',
    )

class ProductoCreate(CreateView):
    model = Producto
    fields='__all__'

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion','marca']

class ProductoDelete(DeleteView):
    model= Producto
    success_url = reverse_lazy('index')

class MarcaCreate(CreateView):
    model = Marca
    fields='__all__'

class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['marca']

class MarcaDelete(DeleteView):
    model= Marca
    success_url = reverse_lazy('marca')


class ProductoDetalles(generic.DetailView):
    model=Producto
class MarcaDetalles(generic.DetailView):

    model = Marca

class ProductoListView(generic.ListView):
    model = Producto
    


    paginate_by = 10


    
