# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
        ('asistencia', '0011_auto_20150107_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('din_hor', models.DateField()),
                ('dfi_hor', models.DateField()),
                ('hin_hor', models.TimeField()),
                ('hfi_hor', models.TimeField()),
                ('est_hor', models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')])),
                ('cre_hor', models.DateTimeField(auto_now_add=True)),
                ('mod_hor', models.DateTimeField(auto_now=True)),
                ('tra_hor', models.ForeignKey(to='personal.Trabajador')),
            ],
            options={
                'verbose_name_plural': 'Horarios',
            },
            bases=(models.Model,),
        ),
    ]
