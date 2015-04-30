# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20150428_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='emp_tra',
            field=models.ForeignKey(verbose_name=b'Empresa', to='asistencia.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nom_tra',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Nombres'),
            preserve_default=True,
        ),
    ]
