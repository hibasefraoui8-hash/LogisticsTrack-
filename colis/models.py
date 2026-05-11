from django.db import models
from client.models import Client

class Statut(models.Model):
    class LibelleChoices(models.TextChoices):
        EN_PREPARATION = 'EN_PREPARATION', 'En préparation'
        EXPEDIE = 'EXPEDIE', 'Expédié'
        EN_COURS_DE_LIVRAISON = 'EN_COURS_DE_LIVRAISON', 'En cours de livraison'
        LIVRE = 'LIVRE', 'Livré'

    libelle = models.CharField(max_length=30, choices=LibelleChoices.choices, unique=True)
    description_etape = models.TextField()

    def __str__(self):
        return self.get_libelle_display()


class Colis(models.Model):
    PRIX_PAR_KG = 10
    expediteur = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='colis_envoyes')
    destinataire = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='colis_recus')
    poids = models.FloatField()
    statut = models.ForeignKey(Statut, on_delete=models.PROTECT)
    date_envoi = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Colis #{self.pk} — {self.expediteur} → {self.destinataire}"
    def frais(self):
        return self.poids * self.PRIX_PAR_KG