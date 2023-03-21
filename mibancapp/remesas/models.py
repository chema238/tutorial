from django.db import models


class Usuarios(models.Model):
    usuario = [
    firstname:= models.CharField(max_length=200),
    lastname:= models.CharField(max_length=200),
    phone:= models.FloatField(max_length=9)
    ]

    def __str__(self):
        return self.lastname
    
class Ordenes(models.Model):
    orden = [ 
    Norden:= models.CharField(max_length=10),
    Beneficiario:= models.CharField(max_length=200),
    Concepto:= models.CharField(max_length=200),
    Bank:= models.CharField(max_length=200),
    IBAN:= models.CharField(max_length=24),
    BIC:= models.CharField(max_length= 20)
    ]
    
    def __str__(self):
        return self.Norden


# Create your models here.
