from django.contrib import admin
from.models import *
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=('idProducto','nombre','categoria','stock','imagen')
    

admin.site.register(Producto,ProductosAdmin)
