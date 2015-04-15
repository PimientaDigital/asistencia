import datetime
from django.http import Http404
from django.shortcuts import render
from asistencia.models import Marca
from personal.models import Trabajador
from asistencia.forms import MarcaForm
from generico.models import Estado
from personal.models import Trabajador

# Create your views here.

TODAY = datetime.date.today()


def marcar(request):
    form = MarcaForm()
    completed = False
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            completed = True
            id_trab = int(form.cleaned_data['trab'])
            trab = Trabajador.objects.get(id=id_trab)
            fec = datetime.date.today()
            est = Estado.objects.get(id=1)
            if not Marca.objects.filter(fec_mar=TODAY).exists():
                hin = datetime.datetime.now()
                hsa = None
                Marca.objects.get_or_create(tra_mar=trab, fec_mar=fec, hin_mar=hin, hsa_mar=hsa, est_mar=est,)
            else:
                hsa = datetime.datetime.now()
                Marca.objects.filter(tra_mar=1, fec_mar=TODAY).update(hsa_mar=hsa)
    context = {'form': form, 'completed': completed}
    template = 'marca.html'
    return render(request, template, context)
