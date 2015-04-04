# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0010_auto_20150106_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia_Semana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_dia_sem', models.CharField(max_length=9, verbose_name='D\xeda')),
            ],
            options={
                'verbose_name_plural': 'Dias de la semana',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]
