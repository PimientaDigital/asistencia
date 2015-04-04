# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0014_auto_20150107_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='dia_hor',
            field=models.ManyToManyField(to='asistencia.Dia_Semana'),
            preserve_default=True,
        ),
    ]
