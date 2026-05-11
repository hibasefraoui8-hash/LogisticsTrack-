from http import client

from django import forms
from .models import Colis

class ColisForm(forms.ModelForm):
    class Meta:
        model = Colis
        fields = ['expediteur', 'destinataire', 'poids', 'statut']
        labels = {
            'expediteur': 'Expéditeur',
            'destinataire': 'Destinataire',
            'poids': 'Poids (kg)',
            'statut': 'Statut',
        }
class  ModifierStatutForm(forms.ModelForm):
    class Meta:
        model=Colis
        fields=['statut']
       