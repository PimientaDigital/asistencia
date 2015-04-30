from django.contrib import admin
from models import *
from actions import export_as_csv
from daterange_filter.filter import DateRangeFilter

# Register your models here.


class HorarioAdmin(admin.ModelAdmin):
    filter_horizontal = ('dia_hor',)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['Dni', 'tra_mar', 'fec_mar', 'hin_mar', 'hsa_mar']
    list_filter = ('tra_mar', 'fec_mar', ('fec_mar', DateRangeFilter))
    search_fields = ('tra_mar__nom_tra',)
    actions = [export_as_csv]

    def Dni(self, instance):
        return instance.tra_mar.dni_tra


admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Tipo_Documento)
admin.site.register(Dia_Semana)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Marca, MarcaAdmin)
