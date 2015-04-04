# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raz_emp', models.CharField(max_length=140, verbose_name=b'Raz\xc3\xb3n Social')),
                ('nom_com_emp', models.CharField(max_length=140, verbose_name=b'Nombre Comercial')),
                ('dir_emp', models.CharField(max_length=140, verbose_name=b'Direcci\xc3\xb3n')),
                ('num_doc_emp', models.CharField(max_length=10, verbose_name=b'N\xc3\xbamero de Documento')),
                ('web_emp', models.URLField(null=True, verbose_name=b'P\xc3\xa1gina Web')),
                ('ema_emp', models.EmailField(max_length=75, null=True, verbose_name=b'Email')),
                ('tel_emp', models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono')),
                ('cre_emp', models.DateTimeField(auto_now_add=True)),
                ('mod_emp', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dir_suc', models.CharField(max_length=140, verbose_name=b'Direcci\xc3\xb3n')),
                ('nom_suc', models.CharField(max_length=20, verbose_name=b'Nombre Sucursal')),
                ('tel_suc', models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono')),
                ('cre_suc', models.DateTimeField(auto_now_add=True)),
                ('mod_suc', models.DateTimeField(auto_now=True)),
                ('Empresa', models.ForeignKey(to='asistencia.Empresa')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
            bases=(models.Model,),
        ),
    ]
