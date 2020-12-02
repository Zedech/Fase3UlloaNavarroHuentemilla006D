from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name='index'),
        path('ropa_hombre/', views.ropa_hombre, name='ropa_hombre'),
        path('zapatilla_hombre/', views.zapatilla_hombre, name='zapatilla_hombre'),
        path('zapatilla_mujer/', views.zapatilla_mujer, name='zapatilla_mujer'),
        path('accesorios/', views.accesorios, name='accesorios'),
        path('contacto/', views.contacto, name='contacto'),
        path('lista/', views.ProductoListView.as_view(), name='lista'),
        path('listaMarcas/', views.MarcaListView.as_view(), name='listamarca'),
        path('producto/<int:pk>', views.ProductoDetalles.as_view(), name='producto-detalles'),
        path('marca/<int:pk>', views.MarcaDetalles.as_view(), name='marca-detalles'),

]
urlpatterns+=[
    
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/<int:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/<int:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
    path('marca/create/', views.MarcaCreate.as_view(), name='marca_create'),
    path('marca/<int:pk>/update/', views.MarcaUpdate.as_view(), name='marca_update'),
    path('marca/<int:pk>/delete/', views.MarcaDelete.as_view(), name='marca_delete'),
    
    ]