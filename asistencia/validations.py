from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from personal.models import Trabajador


def code_validation(value):
    if not Trabajador.objects.filter(pk=value).exists():
        raise ValidationError('Usuario inexistente')
