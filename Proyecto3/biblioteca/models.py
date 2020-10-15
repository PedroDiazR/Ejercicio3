from django.db import models

# Create your models here.

class Prestamo(models.Model):

    codigo = models.AutoField(primary_key=True)
    fechaSalida = models.CharField(max_length=50)
    fechaRegreso = models.CharField(max_length=50)

    def cuota():
        pass

    def __str__(self):
        return str(self.codigo)

class Material(models.Model):

    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    año = models.IntegerField()
    status = models.CharField(max_length=50)
    prestamo = models.ForeignKey('Prestamo', on_delete=models.CASCADE, null=False)

    def altaMaterial():
        pass
    def bajaMaterial():
        pass
    def cambioMaterial():
        pass

    def __str__(self):
        return str(self.tipoMaterial)

class Persona(models.Model):

    tipoPersona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.FloatField()
    prestamo = models.OneToOneField('Prestamo', on_delete = models.CASCADE, null = False)

    def llevarMaterial():
        pass
    def dejarMaterial():
        pass

    def __str__(self):
        return str(self.nombre)

class Libro(Material):

    editorial = models.CharField(max_length=50)
    portada = models.FileField(blank=True)

    def __str__(self):
        return str(self.titulo)

class Revista(Material):

    def __str__(self):
        return str(self.titulo)

class Profesor(Persona):

    numEmpleado = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.nombre)

class Alumno(Persona):

    matricula = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.nombre)
