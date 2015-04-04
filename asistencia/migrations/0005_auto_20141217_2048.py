# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0004_auto_20141217_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='est_emp',
            field=models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empresa',
            name='tip_doc_emp',
            field=models.ForeignKey(default=1, to='asistencia.Tipo_Documento'),
            preserve_default=True,
        ),
    ]
