# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150108_2210'),
        ('generico', '0001_initial'),
        ('asistencia', '0015_horario_dia_hor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fec_mar', models.DateField(verbose_name=b'Fecha de Marca')),
                ('hin_mar', models.TimeField(verbose_name=b'Hora de Ingreso')),
                ('hsa_mar', models.TimeField(null=True, verbose_name=b'Hora de Salida')),
                ('est_mar', models.ForeignKey(verbose_name=b'Estado', to='generico.Estado')),
                ('tra_mar', models.ForeignKey(verbose_name=b'Trabajador', to='personal.Trabajador')),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
            bases=(models.Model,),
        ),
    ]
