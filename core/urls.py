from django.urls import path
from .views import agregar_perro,home, galeria ,listar_perro , eliminar_perro,registro,listado_adoptador,eliminar_adoptador,modificar_adoptador,modificar_perro

urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-perro/', agregar_perro, name="agregar_perro"),
    path('listar-perro/', listar_perro, name="listar_perro"),
    path('eliminar-perro/<id>/', eliminar_perro, name="eliminar_perro"),
    path('registro/', registro, name="registro"),
    path('listar-adoptador/',listado_adoptador,name="listar_adoptador"),
    path('eliminar-adoptador/<run>/',eliminar_adoptador,name="eliminar_adoptador"),
    path('modificar-adoptador/<run>/',modificar_adoptador,name="modificar_adoptador"),
    path('modificar-perro/<id>/',modificar_perro,name="modificar_perro")
]
