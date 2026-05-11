
from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from colis.models import Colis

def rechercher(request):
    colis = None
    query = request.GET.get('q')
    if query:
        colis = Colis.objects.filter(
            expediteur__nom__icontains=query
        ) | Colis.objects.filter(
            destinataire__nom__icontains=query
        )
    return render(request, 'client/dashboard_client.html', {'colis': colis, 'query': query})

def detail_colis(request, colis_id):
    colis = get_object_or_404(Colis, id=colis_id)
    return render(request, 'client/detail_colis.html', {'colis': colis})


