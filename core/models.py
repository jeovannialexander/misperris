from django.db import models

# Create your models here.
class Raza(models.Model):

    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Region(models.Model):
    #id_region = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"


class Ciudad(models.Model):
    #id_ciudad = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"  


class TipoVivienda(models.Model):
    #id_vivienda = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion 

    class Meta:
        verbose_name = "Tipo Vivienda"
        verbose_name_plural = "Tipos de Vivienda"

class Postulante(models.Model):
    run = models.CharField(max_length=50,unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField(auto_now=True)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.run

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"                



class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre               



class Mascota(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    raza  = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero  = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_ingreso  = models.DateField(max_length=50)
    fecha_nacimiento  = models.DateField(max_length=50)
    estado  = models.ForeignKey(Estado, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="mascotas", null=True)
    
    
    #clave foranea
    
    
   

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Mascota"
        verbose_name_plural = "Mascotas"