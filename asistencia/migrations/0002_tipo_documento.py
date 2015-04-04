# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('des_tip_doc', models.CharField(max_length=50, verbose_name=b'Tipo de Documento')),
                ('est_tipo_doc', models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(1, b'Activo'), (2, b'Inactivo'), (3, b'Eliminado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
