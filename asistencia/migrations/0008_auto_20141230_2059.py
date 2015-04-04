# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0007_area_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_tra', models.CharField(max_length=140, verbose_name=b'Nombres')),
                ('app_tra', models.CharField(max_length=30, verbose_name=b'Apellido Paterno')),
                ('apm_tra', models.CharField(max_length=30, verbose_name=b'Apellido Materno')),
                ('num_doc_tra', models.CharField(max_length=15, verbose_name=b'Num. Doc')),
                ('eda_tra', models.SmallIntegerField(null=True, verbose_name=b'Edad')),
                ('est_tra', models.CharField(default=1, max_length=1, verbose_name=b'Estado', choices=[(b'1', b'Activo'), (b'2', b'Inactivo'), (b'3', b'Eliminado')])),
                ('sex_tra', models.CharField(default=1, max_length=1, verbose_name=b'Sexo', choices=[(b'1', b'Femenino'), (b'2', b'Masculino')])),
                ('cre_tra', models.DateTimeField(auto_now_add=True)),
                ('mod_tra', models.DateTimeField(auto_now=True)),
                ('are_tra', models.ForeignKey(to='asistencia.Area', null=True)),
                ('car_tra', models.ForeignKey(to='asistencia.Cargo', null=True)),
                ('tip_doc_tra', models.ForeignKey(default=1, to='asistencia.Tipo_Documento')),
            ],
            options={
                'verbose_name_plural': 'Trabajadores',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='mod_are',
            new_name='mod_car',
        ),
    ]
