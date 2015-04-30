from django.db import models

# Create your models here.

class Trabajador(models.Model):
    nom_tra = models.CharField('Nombres', max_length=80, blank=True, null=True)
    app_tra = models.CharField('Apellido P.', max_length=40, blank=True, null=True)
    apm_tra = models.CharField('Apellido M.', max_length=40, blank=True, null=True)
    dni_tra = models.CharField('dni', max_length=8, primary_key=True)
    emp_tra = models.ForeignKey('asistencia.Empresa', verbose_name='Empresa', blank=True, null=True)

    def __unicode__(self):
        return '%s - %s - %s' % (self.nom_tra, self.app_tra, self.apm_tra)
    class meta:
        verbose_name_plural = 'Trabajadores'
    
