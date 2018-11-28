from django.urls import path
from .views import listar_perro, agregar_perro, eliminar_perro,modificar_perro,agregar_token

urlpatterns = [
    
    path('agregar-perro/', agregar_perro, name="api_agregar_perro"),
    path('listar-perro/', listar_perro, name="api_listar_perro"),
    path('eliminar-perro/<id>/', eliminar_perro, name="api_eliminar_perro"),
    path('modificar-perro/', modificar_perro, name="api_modificar_auto"),
        path('agregar-token/', agregar_token, name="api_agregar_token"),
]