# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0003_tipo_documento_long_tip_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_documento',
            name='est_tipo_doc',
            field=models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')]),
            preserve_default=True,
        ),
    ]
