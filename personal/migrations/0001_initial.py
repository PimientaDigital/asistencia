# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_tra', models.CharField(max_length=80, verbose_name=b'Nombres')),
                ('app_tra', models.CharField(max_length=40, null=True, verbose_name=b'Apellido P.')),
                ('apm_tra', models.CharField(max_length=40, null=True, verbose_name=b'Apellido M.')),
                ('dni_tra', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
