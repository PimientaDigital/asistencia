# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0006_sucursal_est_suc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_are', models.CharField(max_length=140, verbose_name=b'Descripci\xc3\xb3n')),
                ('cre_are', models.DateTimeField(auto_now_add=True)),
                ('mod_are', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_car', models.CharField(max_length=140, verbose_name=b'Cargo')),
                ('cre_car', models.DateTimeField(auto_now_add=True)),
                ('mod_are', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
    ]
