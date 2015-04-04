from django.db import models

# Create your models here.

class Estado(models.Model):
    des_est = models.CharField('Estado', max_length=15)
    def __unicode__(self):
        return self.des_est
    class Meta:
        verbose_name_plural = 'Estados'