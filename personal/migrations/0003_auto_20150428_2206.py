# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150108_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='id',
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='dni_tra',
            field=models.CharField(max_length=8, serialize=False, verbose_name=b'dni', primary_key=True),
            preserve_default=True,
        ),
    ]
