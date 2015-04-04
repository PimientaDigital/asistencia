# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0015_horario_dia_hor'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='emp_tra',
            field=models.ForeignKey(default=1, verbose_name=b'Empresa', to='asistencia.Empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='dni_tra',
            field=models.CharField(max_length=8, verbose_name=b'dni'),
            preserve_default=True,
        ),
    ]
