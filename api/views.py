from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from core.models import Mascota, Raza, Genero , Estado

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from fcm_django.models import FCMDevice
# Create your views here.

#crearemos un view que muestre el listado de automoviles
#en formato json
@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    #obtenemos el token
    token = bodyDict['token']

    #primero verificamos que el token no exista en la BD para guardarlo
    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}), content_type="application/json")


    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True


    #solo si el usuario esta auntenticado lo asociaremos con el token
    if request.user.is_authenticated:
        dispositivo.user = request.user
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")



def listar_perro(request):
    auto = Mascota.objects.all()
    #transformamos los datos a json
    autosJson = serializers.serialize('json', auto)

    #mostramos el json en el navegador
    return HttpResponse(autosJson, content_type="application/json")

#POST
@csrf_exempt
@require_http_methods(['POST'])
def agregar_perro(request):
    
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    auto = Mascota()
    auto.nombre = bodyDict['nombre']
    auto.raza = Raza(id=bodyDict['raza_id'])
    auto.genero  = Genero(id=bodyDict['genero_id'])
    auto.fecha_ingreso = bodyDict['fecha_ingreso']
    auto.fecha_nacimiento = bodyDict['fecha_nacimiento']
    auto.estado  = Estado(id=bodyDict['estado_id'])
    auto.imagen = bodyDict['imagen']

    try:
        auto.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_perro(request, id):

    try:
        #primero buscamos el automovil que eliminaremos
        auto = Mascota.objects.get(id=id)
        auto.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminado correctamente'}),
         content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"no se ha podido eliminar"}),
        content_type="application/json")
    

#POST
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_perro(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos el automovil en la BBDD
    auto = Mascota()
    auto.nombre = bodyDict['nombre']
    auto.raza = Raza(id=bodyDict['raza_id'])
    auto.genero  = Genero(id=bodyDict['genero_id'])
    auto.fecha_ingreso = bodyDict['fecha_ingreso']
    auto.fecha_nacimiento = bodyDict['fecha_nacimiento']
    auto.estado  = Estado(id=bodyDict['estado_id'])
    auto.imagen = bodyDict['imagen']

    try:
        auto.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido modificar'}), content_type="application/json")


# Create your views here.
