from django.contrib import admin
from colis.models import Colis, Statut

class ColisAdmin(admin.ModelAdmin):
    list_display = ('id', 'expediteur', 'destinataire', 'poids', 'statut', 'date_envoi')
    list_editable = ('statut',)  # modifier statut directement depuis la liste
    search_fields = ('expediteur__nom', 'destinataire__nom')
    list_filter = ('statut',)


class StatutAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description_etape')
    search_fields = ('libelle',)
    
admin.site.register(Colis,ColisAdmin)
admin.register(Statut, StatutAdmin)


