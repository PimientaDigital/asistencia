# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('des_est', models.CharField(max_length=15, verbose_name=b'Estado')),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
            bases=(models.Model,),
        ),
    ]
