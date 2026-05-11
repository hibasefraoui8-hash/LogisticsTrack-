from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from client.forms import ClientForm
from .models import Colis
from .forms import ColisForm, ModifierStatutForm
from django.contrib.auth import authenticate, login, logout


def login_agent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_colis')
        else:
            return render(request, 'colis/login.html', {'error': 'Identifiants incorrects'})
    return render(request, 'colis/login.html')

def logout_agent(request):
    logout(request)
    return redirect('login_agent')
@login_required
def enregistrer_colis(request):
    form = ColisForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_colis')
    return render(request, 'colis/enregistrer_colis.html', {'form': form})

@login_required
def modifier_colis(request, colis_id):
    colis = get_object_or_404(Colis, id=colis_id)
    form = ColisForm(request.POST or None, instance=colis)
    if form.is_valid():
            form.save()
            return redirect('liste_colis')
    return render(request, 'colis/enregistrer_colis.html', {'form': form})

@login_required
def modifier_statut(request, colis_id):
    colis = get_object_or_404(Colis, id=colis_id)
    if request.method == 'POST':
        form = ModifierStatutForm(request.POST, instance=colis)
        if form.is_valid():
            form.save()
            return redirect('liste_colis')
    else:
        form = ModifierStatutForm(instance=colis)
    return render(request, 'colis/enregistrer_colis.html', {'form': form, 'colis': colis})

@login_required
def supprimer_colis(request, colis_id):
    colis = get_object_or_404(Colis, id=colis_id)
    colis.delete()
    return redirect('liste_colis')

@login_required
def liste_colis(request):
    colis = Colis.objects.all().order_by('-date_envoi')
    return render(request, 'colis/liste_colis.html', {'colis': colis})

@login_required
def rechercher(request):
    colis = Colis.objects.all()
    query = request.GET.get('q')
    statut = request.GET.get('statut')

    if query:
        colis = colis.filter(expediteur__nom__icontains=query) | \
                colis.filter(destinataire__nom__icontains=query)
    if statut:
        colis = colis.filter(statut__libelle=statut)

    return render(request, 'colis/liste_colis.html', {'colis': colis, 'query': query, 'statut': statut})

@login_required
def historique(request):
    colis = Colis.objects.all().order_by('-date_envoi')
    date_debut = request.GET.get('date_debut')
    date_fin = request.GET.get('date_fin')

    if date_debut:
        colis = colis.filter(date_envoi__gte=date_debut)
    if date_fin:
        colis = colis.filter(date_envoi__lte=date_fin)

    return render(request, 'colis/historique.html', {'colis': colis})
@login_required
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enregistrer_colis')
    else:
        form = ClientForm()
    return render(request, 'colis/ajouter_client.html', {'form': form})