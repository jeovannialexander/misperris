from django.shortcuts import render,redirect
from .models import Mascota,Estado,Raza,Genero,Ciudad,Region,TipoVivienda,Postulante

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
   

   return render(request, 'core/home.html', {
        'mascotas':Mascota.objects.all()
    })



def galeria(request):
    return render(request,'core/galeria.html')

@login_required
def agregar_perro(request):
    razas  = Raza.objects.all()
    estados  = Estado.objects.all()
    generos  = Genero.objects.all()
    mascotas = Mascota.objects.all()
    #enviamos las marcas hacia el template
    variables = {
        'razas':razas,
        'estados':estados,
        'generos':generos,
        'mascotas':mascotas

    }

    #preguntaremos si es POST
    if request.POST:
        #si la peticion es POST obtendremos los datos
        auto = Mascota()
        auto.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id  = request.POST.get('cboRaza')
        auto.raza = raza
        genero = Genero()
        genero.id  = request.POST.get('cboGenero')
        auto.genero = genero
        auto.fecha_ingreso  = request.POST.get('txtIngreso')
        auto.fecha_nacimiento  = request.POST.get('txtNacimiento')
        auto.imagen = request.FILES.get('txtImagen')
       

        #la marca es una colaboracion de clases
        #por lo tanto para obtener el combo primero
        #crearemos un objeto Marca
        estado = Estado()
        estado.id  = request.POST.get('cboEstado')
        #guardamos la marca completo dentro del auto
        auto.estado = estado


        auto.save()
        #procedemos a guardar el auto en la BBDD
        try:
            
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/agregar_perro.html', variables)

def listar_perro(request):

    mascota = Mascota.objects.all()

    return render(request,'core/listar_perro.html',{
        'mascotas':mascota
    })

   

def eliminar_perro(request, id):
    #primer paso buscamos el automovil
    auto = Mascota.objects.get(id=id)

    #procedemos a eliminar
    auto.delete()
    
    #redirigimos al usuario de vuelta al listado
    return redirect('listar_perro')

def registro(request):
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    tipoviviendas = TipoVivienda.objects.all()

    variables = {
        'regiones':regiones,
        'ciudades':ciudades,
        'tipoviviendas':tipoviviendas
    }
    
    if request.POST:
        postul = Postulante()
        postul.run = request.POST.get('txtRun')
        postul.nombre = request.POST.get('txtNombre')
        postul.apellido = request.POST.get('txtApellido')
        postul.fechaNacimiento = request.POST.get('Fecha')
        postul.email = request.POST.get('txtEmail')
        postul.telefono = request.POST.get('txtTelefono')
        #region
        region = Region()
        region.id = request.POST.get('cboRegion')
        postul.region = region
        #ciudad
        ciudad = Ciudad()                
        ciudad.id = request.POST.get('cboCiudad')        
        postul.ciudad = ciudad
        #tipo vivienda        
        tipovivienda = TipoVivienda()
        tipovivienda.id = request.POST.get('cboTipoVivienda')
        postul.tipoVivienda = tipovivienda

        try:
            postul.save()            
            variables['mensaje'] = 'Guardado correctamente'            
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/registro.html', variables)    


def listado_adoptador(request):

    adoptador = Postulante.objects.all()

    return render(request,'core/listar_adoptador.html',{
        'adoptadores':adoptador
    })


def eliminar_adoptador(request, run):
    adoptador = Postulante.objects.get(run=run)

    try:
        adoptador.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request,mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mesaje)
    return redirect('listado_adoptador')

def modificar_adoptador(request,run):
    adoptador = Postulante.objects.get(run=run)
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    tipoviviendas = TipoVivienda.objects.all()

    variables = {
        'adoptador':adoptador,
        'regiones':regiones,
        'ciudades':ciudades,
        'tipoviviendas':tipoviviendas
    }

    return render(request,'core/modificar_adoptador.html',variables)


def modificar_perro(request,id):
    mascota = Mascota.objects.get(id=id)
    estados = Estado.objects.all()
    generos = Genero.objects.all()
    razas = Raza.objects.all()
   

    variables = {
        'razas':razas,
        'estados':estados,
        'generos':generos
    }

    if request.POST:
        #si la peticion es POST obtendremos los datos
        auto = Mascota()
        auto.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id  = request.POST.get('cboRaza')
        auto.raza = raza
        genero = Genero()
        genero.id  = request.POST.get('cboGenero')
        auto.genero = genero
        auto.fecha_ingreso  = request.POST.get('txtIngreso')
        auto.fecha_nacimiento  = request.POST.get('txtNacimiento')
        auto.imagen = request.FILES.get('txtImagen')
       

        #la marca es una colaboracion de clases
        #por lo tanto para obtener el combo primero
        #crearemos un objeto Marca
        estado = Estado()
        estado.id  = request.POST.get('cboEstado')
        #guardamos la marca completo dentro del auto
        auto.estado = estado


        auto.save()
        #procedemos a guardar el auto en la BBDD
        try:
            
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/agregar_perro.html', variables)

def listar_perro(request):

    mascota = Mascota.objects.all()

    return render(request,'core/listar_perro.html',{
        'mascotas':mascota
    })

   

def eliminar_perro(request, id):
    #primer paso buscamos el automovil
    auto = Mascota.objects.get(id=id)

    #procedemos a eliminar
    auto.delete()
    
    #redirigimos al usuario de vuelta al listado
    return redirect('listar_perro')

def registro(request):
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    tipoviviendas = TipoVivienda.objects.all()

    variables = {
        'regiones':regiones,
        'ciudades':ciudades,
        'tipoviviendas':tipoviviendas
    }
    
    if request.POST:
        postul = Postulante()
        postul.id = int(request.POST.get('txtId'))
        postul.run = request.POST.get('txtRun')
        postul.nombre = request.POST.get('txtNombre')
        postul.apellido = request.POST.get('txtApellido')
        postul.fechaNacimiento = request.POST.get('Fecha')
        postul.email = request.POST.get('txtEmail')
        postul.telefono = int(request.POST.get('txtTelefono'))
        #region
        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        postul.region = region
        #ciudad
        ciudad = Ciudad()                
        ciudad.id = int(request.POST.get('cboCiudad'))        
        postul.ciudad = ciudad
        #tipo vivienda        
        tipovivienda = TipoVivienda()
        tipovivienda.id = int(request.POST.get('cboTipoVivienda'))
        postul.tipoVivienda = tipovivienda

        try:
            postul.save()            
            variables['mensaje'] = 'Guardado correctamente'            
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/modificar-perro.html', variables)   
