import datetime
from django.http import Http404
from django.shortcuts import render, redirect
from asistencia.models import Marca
from personal.models import Trabajador
from asistencia.forms import MarcaForm
from generico.models import Estado
from personal.models import Trabajador
from asistencia.models import Marca

# Create your views here.


def marcar(request):
    form = MarcaForm()
    completed = False
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            completed = True
            trab = Trabajador.objects.get(id=int(form.cleaned_data['trab']))
            fec = datetime.date.today()
            hin = datetime.datetime.time(datetime.datetime.now())
            hsa = None
            est = Estado.objects.get(id=1)
            Marca.objects.get_or_create(tra_mar=trab,fec_mar=fec,hin_mar=hin,hsa_mar=hsa,est_mar=est,)
    context = {'form': form, 'completed': completed}
    template = 'marca.html'
    return render(request, template, context)
