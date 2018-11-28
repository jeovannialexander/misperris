from django.contrib import admin

# Register your models here.

from .models import Mascota, Estado , Raza , Genero,Postulante,TipoVivienda,Ciudad,Region

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    #declaramos una tupla
    list_display = ('nombre', 'raza', 'genero', 'fecha_ingreso','fecha_nacimiento','estado')
    search_fields = ['nombre', 'raza']
    #agregaremos un filtro personalizado en el admin
   

class MisPerrisAdmin(admin.ModelAdmin):
    list_display = ('run', 'nombre', 'apellido', 'fechaNacimiento','email','telefono')
    search_fields = ['run', 'nombre']
    list_filter = ('run',)    

admin.site.register(Estado)
admin.site.register(Raza)
admin.site.register(Genero)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(TipoVivienda)
admin.site.register(Postulante, MisPerrisAdmin)
admin.site.register(Mascota, MascotaAdmin)