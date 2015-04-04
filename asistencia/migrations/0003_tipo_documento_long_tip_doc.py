# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_tipo_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_documento',
            name='long_tip_doc',
            field=models.SmallIntegerField(default=8, verbose_name=b'Longitud m\xc3\xa1xima'),
            preserve_default=True,
        ),
    ]
