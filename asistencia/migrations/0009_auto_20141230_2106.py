# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0008_auto_20141230_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sucursal',
            old_name='Empresa',
            new_name='emp_suc',
        ),
    ]
