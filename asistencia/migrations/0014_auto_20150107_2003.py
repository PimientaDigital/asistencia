# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0013_auto_20150107_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario_dias',
            name='dia_hor_dia',
        ),
        migrations.RemoveField(
            model_name='horario_dias',
            name='hor_hor_dia',
        ),
        migrations.DeleteModel(
            name='Horario_Dias',
        ),
    ]
