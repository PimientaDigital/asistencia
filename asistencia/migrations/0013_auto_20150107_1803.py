# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0012_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario_Dias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('est_hor_dia', models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')])),
                ('cre_hor_dia', models.DateTimeField(auto_now_add=True)),
                ('mod_hor_dia', models.DateTimeField(auto_now=True)),
                ('dia_hor_dia', models.ForeignKey(verbose_name='D\xeda', to='asistencia.Dia_Semana')),
                ('hor_hor_dia', models.ForeignKey(verbose_name='Horario', to='asistencia.Horario')),
            ],
            options={
                'verbose_name_plural': 'Horario por Dias',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dfi_hor',
            field=models.DateField(verbose_name=b'Hasta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='horario',
            name='din_hor',
            field=models.DateField(verbose_name=b'Desde'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='horario',
            name='hfi_hor',
            field=models.TimeField(verbose_name=b'H. Salida'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='horario',
            name='hin_hor',
            field=models.TimeField(verbose_name=b'H. Ingreso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='horario',
            name='tra_hor',
            field=models.ForeignKey(verbose_name=b'Trabajador', to='personal.Trabajador'),
            preserve_default=True,
        ),
    ]
