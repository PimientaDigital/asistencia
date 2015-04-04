from django.contrib import admin
from models import *

# Register your models here.


class HorarioAdmin(admin.ModelAdmin):
    filter_horizontal = ('dia_hor',)

admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Tipo_Documento)
admin.site.register(Dia_Semana)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Marca)
