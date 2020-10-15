from django.contrib import admin
from .models import *

class MaterialInline(admin.TabularInline):
    model = Material
    fields = ['tipoMaterial','autor','titulo','año','status']
    extra = 0

class PersonaInline(admin.TabularInline):
    model = Persona
    fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']

class PrestamoAdmin(admin.ModelAdmin):

    inlines = [MaterialInline, PersonaInline]

class LibroAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status','editorial']
    list_display_links = ['tipoMaterial','codigo','autor','titulo','año','status','editorial']
    search_fields = ['tipoMaterial','codigo','autor','titulo','año','status','editorial']
    fieldsets = (
        ("Descripcion", {
            'fields':('editorial','tipoMaterial','titulo','año','status','portada')
        }),
        ('Autor', {
            'fields':('autor',)
        }),
    )

class RevistaAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status']
    list_display_links = ['tipoMaterial','codigo','autor','titulo','año','status']
    search_fields = ['tipoMaterial','codigo','autor','titulo','año','status']
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoMaterial','titulo','año','status')
        }),
        ('Autor', {
            'fields':('autor',)
        }),
    )

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['matricula','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    list_display_links = ['matricula','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    search_fields = ['matricula','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoPersona','nombre','apellido','numLibros','adeudo')
        }),
        ('Contacto', {
            'fields':('correo','telefono',)
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['numEmpleado','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    list_display_links = ['numEmpleado','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    search_fields = ['numEmpleado','tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo']
    fieldsets = (
        ("Descripcion", {
            'fields':('tipoPersona','nombre','apellido','numLibros','adeudo')
        }),
        ('Contacto', {
            'fields':('correo','telefono',)
        }),
    )

# Register your models here.

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Material)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
