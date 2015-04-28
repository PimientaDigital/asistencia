# -*- coding: utf-8 -*-
from model_report.report import reports, ReportAdmin
from model_report.utils import (usd_format, avg_column, sum_column, count_column)

from models import Marca


class ReporteMarcas(ReportAdmin):
    model = Marca
    fields = [
        'fec_mar',
        'tra_mar',
    ]
    list_group_by = ('fec_mar', 'tra_mar',)
    list_filter = ('trabajador',)
    type = 'report'
    override_field_labels = {
        'fec_mar': lambda x, y: ('fec_mar'),
    }

reports.register('Reporte-Marcas', ReporteMarcas)
