from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'adresse', 'telephone']
        labels = {
            'nom': 'Nom',
            'adresse': 'Adresse',
            'telephone': 'Téléphone',
        }