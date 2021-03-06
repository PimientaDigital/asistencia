import datetime
from django.shortcuts import render
from asistencia.models import Marca
from personal.models import Trabajador
from asistencia.forms import MarcaForm
from generico.models import Estado
from personal.models import Trabajador
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Create your views here.

TODAY = datetime.date.today()


def marcar(request):
    form = MarcaForm()
    completed = False
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            completed = True
            id_trab = str(form.cleaned_data['trab'])
            trab = Trabajador.objects.get(dni_tra=id_trab)
            fec = datetime.date.today()
            est = Estado.objects.get(id=1)
            if not Marca.objects.filter(fec_mar=TODAY, tra_mar=id_trab).exists():
                hin = datetime.datetime.now()
                hsa = None
                Marca.objects.get_or_create(tra_mar=trab, fec_mar=fec, hin_mar=hin, hsa_mar=hsa, est_mar=est,)
                messages.success(request, "Marca Registrada")
                url = reverse('mensaje')
                return HttpResponseRedirect(url)
            else:
                hsa = datetime.datetime.now()
                Marca.objects.filter(tra_mar=id_trab, fec_mar=TODAY).update(hsa_mar=hsa)
                messages.success(request, "Marca Registrada")
                url = reverse('mensaje')
                return HttpResponseRedirect(url)
    context = {'form': form, 'completed': completed}
    template = 'marca.html'
    return render(request, template, context)


def mensaje(request):
    template = 'marca_registrada.html'
    return render(request, template)
