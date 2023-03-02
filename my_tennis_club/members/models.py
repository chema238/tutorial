from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)#es un campo de texto y contendrá el nombre de los miembros.firstname
  lastname = models.CharField(max_length=255)#es también un campo de texto, con el apellido del miembro.lastname
  phone = models.IntegerField(null=True)
  joined_date= models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
# Create your models here.
