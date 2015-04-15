# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from validations import code_validation


class MarcaForm(forms.Form):
    trab = forms.CharField(
        label=_(u'Código'),
        max_length=5,
        validators=[code_validation]
        )
