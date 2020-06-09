from .models import Configuracion
import json
import requests
import datetime
from dateutil.relativedelta import relativedelta

def Valida_fecha(fecha):
    if fecha.day < 15:
        fecha = fecha - relativedelta(months=1)
    return fecha

def Consulta_tipo(monto,plazo):
    if plazo < 90 and monto <= 5000:
        return 26

    if plazo < 90 and monto > 5000:
        return 25

    if plazo >= 90 and monto <= 50:
        return 45

    if plazo >= 90 and monto <= 200 and monto > 50:
        return 44

    if plazo >= 90 and monto <= 5000 and monto > 200:
        return 35

    if plazo >= 90 and monto > 5000:
        return 34

def Get_data(fecha):
    apikey = Configuracion.objects.get(variable= "apikey" ).valor
    urlapi = Configuracion.objects.get(variable= "urlapi" ).valor
    url = urlapi + str(fecha.year) + "/" + str(fecha.month) + "?apikey=" + str(apikey) + "&formato=json"
    response = requests.request("GET", url)
    return json.loads(response.text)