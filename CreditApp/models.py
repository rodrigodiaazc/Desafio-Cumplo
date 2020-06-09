from django.db import models

# Create your models here.


class Configuracion(models.Model):
    variable = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.variable + ' - ' + self.valor
    
    