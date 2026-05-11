from django.db import models

# Create your models here.
class Client(models.Model):
    nom=models.CharField( max_length=250)
    adresse=models.CharField(max_length=250)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom