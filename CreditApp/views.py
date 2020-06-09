from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from .models import Configuracion
from .reglas import Valida_fecha
from .reglas import Consulta_tipo
from .reglas import Get_data

@login_required
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        fechaTMC = Valida_fecha(datetime.datetime.strptime(str(request.POST.get("FechaTMC", False)), '%Y-%m-%d'))
        tipo = Consulta_tipo(float(request.POST.get("Monto", False)), float(request.POST.get("Plazo", False) ))
        try:
            data_json = Get_data(fechaTMC)
        except Exception as ex:
            messages.add_message(request, messages.INFO, 'Error de comunicación')
            return HttpResponseRedirect('/')
        
        try:
            for data in data_json['TMCs']:
                if int(tipo) == int(data['Tipo']):
                    tmc = dict(data)
            context = {
                "data" : tmc,
                "fecha" : str(request.POST.get("FechaTMC", False)),
                "monto" : float(request.POST.get("Monto", False)),
                "plazo" : int(request.POST.get("Plazo", False))
            }
            return render(request,"CreditApp/index.html", context)
        except Exception as ex:
            if data_json['CodigoError']:
                messages.add_message(request, messages.INFO, 'No se encontraron datos para la fecha especificada.')
                return HttpResponseRedirect('/')

    return render(request,"CreditApp/index.html")

