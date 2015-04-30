# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20150430_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='nom_tra',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Nombres', blank=True),
            preserve_default=True,
        ),
    ]
