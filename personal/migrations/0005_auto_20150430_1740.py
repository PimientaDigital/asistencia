# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20150430_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='apm_tra',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Apellido M.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='app_tra',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Apellido P.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='emp_tra',
            field=models.ForeignKey(verbose_name=b'Empresa', blank=True, to='asistencia.Empresa', null=True),
            preserve_default=True,
        ),
    ]
