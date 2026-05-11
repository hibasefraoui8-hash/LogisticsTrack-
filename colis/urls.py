from . import views
from django.urls import path
urlpatterns = [
    
    path("",views.login_agent,name="login_agent"),
    path("logout/",views.logout_agent,name="logout_agent"),
    path("liste/",views.liste_colis,name="liste_colis"),
    path("ajouter_client/",views.ajouter_client,name="ajouter_client"),
    path("enregistrer/",views.enregistrer_colis,name="enregistrer_colis"),
    path('modifier/<int:colis_id>/', views.modifier_colis, name='modifier_colis'),
    path('modifier-statut/<int:colis_id>/', views.modifier_statut, name='modifier_statut'),
    path('supprimer/<int:colis_id>/', views.supprimer_colis, name='supprimer_colis'),
    path('rechercher/', views.rechercher, name='rechercher'),
    path('historique/', views.historique, name='historique'),
]
