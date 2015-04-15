# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Tipo_Documento(models.Model):
    EST_TIP_DOC = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
        ('3', 'Eliminado'),
)
    des_tip_doc = models.CharField('Tipo de Documento', max_length=50)
    long_tip_doc = models.SmallIntegerField('Longitud máxima', default=8)
    est_tipo_doc = models.CharField('Estado', max_length=1, choices=EST_TIP_DOC, default=1)

    def __unicode__(self):
        return self.des_tip_doc

    class meta:
        verbose_name_plural = u'Tipos de documento'


class Empresa(models.Model):
    EST_EMP = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
        ('3', 'Eliminado'),
    )
    raz_emp = models.CharField('Razón Social', max_length=140)
    nom_com_emp = models.CharField('Nombre Comercial', max_length=140)
    dir_emp = models.CharField('Dirección', max_length=140)
    num_doc_emp = models.CharField('Número de Documento', max_length=10)
    web_emp = models.URLField('Página Web', null=True)
    ema_emp = models.EmailField('Email', null=True)
    tel_emp = models.CharField('Teléfono', max_length=12)
    est_emp = models.CharField('Estado', max_length=1, choices=EST_EMP, default=1)
    cre_emp = models.DateTimeField(auto_now_add=True)
    mod_emp = models .DateTimeField(auto_now=True)
    tip_doc_emp = models.ForeignKey(Tipo_Documento, default=1)

    def __unicode__(self):
        return self.raz_emp


class Sucursal(models.Model):
    EST_SUC = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
        ('3', 'Eliminado'),
    )
    dir_suc = models.CharField('Dirección', max_length=140)
    nom_suc = models.CharField('Nombre Sucursal', max_length=20)
    tel_suc = models.CharField('Teléfono', max_length=12)
    est_suc = models.CharField('Estado', max_length=1, choices=EST_SUC, default=1)
    cre_suc = models.DateTimeField(auto_now_add=True)
    mod_suc = models .DateTimeField(auto_now=True)
    emp_suc = models.ForeignKey(Empresa)

    def __unicode__(self):
        return '%s - %s' % (self.emp_suc, self.nom_suc)

    class Meta:
        verbose_name_plural = "Sucursales"
        

class Dia_Semana(models.Model):
    nom_dia_sem = models.CharField(u'Día', max_length=9)

    def __unicode__(self):
        return self.nom_dia_sem

    class Meta:
        verbose_name_plural = u'Dias de la semana'


class Horario(models.Model):
    EST_HOR = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
        ('3', 'Eliminado'),
    )
    din_hor = models.DateField('Desde')
    dfi_hor = models.DateField('Hasta')
    hin_hor = models.TimeField('H. Ingreso')
    hfi_hor = models.TimeField('H. Salida')
    est_hor = models.CharField('Estado', max_length=1, choices=EST_HOR, default=1)
    cre_hor = models.DateTimeField(auto_now_add=True)
    mod_hor = models.DateTimeField(auto_now=True)
    tra_hor = models.ForeignKey('personal.Trabajador', verbose_name='Trabajador')
    dia_hor = models.ManyToManyField(Dia_Semana)

    def __unicode__(self):
        return '%s - %s' % ('horario', self.tra_hor)

    class Meta:
        verbose_name_plural = u'Horarios'


class Marca(models.Model):
    tra_mar = models.ForeignKey('personal.Trabajador', verbose_name='Trabajador')
    fec_mar = models.DateField('Fecha de Marca')
    hin_mar = models.TimeField('Hora de Ingreso')
    hsa_mar = models.TimeField('Hora de Salida', null=True)
    est_mar = models.ForeignKey('generico.Estado', verbose_name='Estado')

    def __unicode__(self):
        return '%s - %s' % (self.tra_mar, self.fec_mar)

    class Meta:
        verbose_name_plural = u'Marcas'
