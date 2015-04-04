# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0009_auto_20141230_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='are_tra',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='car_tra',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='tip_doc_tra',
        ),
        migrations.DeleteModel(
            name='Trabajador',
        ),
    ]
