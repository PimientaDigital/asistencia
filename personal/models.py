from django.db import models

# Create your models here.

class Trabajador(models.Model):
    nom_tra = models.CharField('Nombres', max_length=80)
    app_tra = models.CharField('Apellido P.', max_length=40, null=True)
    apm_tra = models.CharField('Apellido M.',max_length=40, null=True)
    dni_tra = models.CharField('dni',max_length=8)
    emp_tra = models.ForeignKey('asistencia.Empresa', verbose_name='Empresa')

    def __unicode__(self):
        return '%s - %s' % (self.nom_tra, self.app_tra)
    class meta:
        verbose_name_plural = 'Trabajadores'
    