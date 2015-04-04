# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import *
from validations import code_validation


class MarcaForm(forms.Form):
    trab = forms.CharField(
            label = _(u'Código'),
            max_length=5,
            validators = [code_validation]
        )
