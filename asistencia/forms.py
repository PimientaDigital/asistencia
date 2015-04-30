# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from validations import code_validation
from django.forms import ModelForm, CharField, TextInput


class MarcaForm(forms.Form):
    trab = forms.CharField(
        label=_(u'Código'),
        max_length=8,
        validators=[code_validation]
        )
