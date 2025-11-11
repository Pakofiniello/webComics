from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Manga, Chapter, Artist, tab_valutazioni, User, UserProfile
from django.shortcuts import get_object_or_404, redirect
from .forms import LoginForm, register_form
from rest_framework import serializers 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import sys, json
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        print("\033[38;5;46m[LOGIN] Utente autenticato:", request.user.username, "\033[0m", file=sys.stderr)
    else:
        print("\033[38;5;208m[LOGIN] Utente anonimo è entrato nel sito\033[0m", file=sys.stderr)

    popular_artists = Artist.objects.all()[:4]
    top_mangas = Manga.objects.all()[:4]
    template = loader.get_template("Fumetti/index.html")
    last_chapters = Chapter.objects.all()[:4]
    context = {'last_chapters' : last_chapters,
               'top_mangas' : top_mangas,
               'popular_artists' : popular_artists}
    return HttpResponse(template.render(context,request))


def fumetto_detail(request, fumetto_id):

    fumetto = get_object_or_404(Manga, id=fumetto_id)
    if request.method == "POST":
        stelle = request.POST.get("rating")
        if stelle and stelle.isdigit() and 1 <= int(stelle) <= 5:
            stelle = int(stelle)
            valutazione = tab_valutazioni.objects.filter(manga_riferimento=fumetto).first()
            if valutazione:
                valutazione.insert += 1
                valutazione.somma_stelle += stelle
                valutazione.media = valutazione.somma_stelle / valutazione.insert
                valutazione.save()
            else:
                tab_valutazioni.objects.create(
                    manga_riferimento=fumetto,
                    insert=1,
                    somma_stelle=stelle,
                    media=stelle
                )

        return redirect(request.path)

    valutazione = tab_valutazioni.objects.filter(manga_riferimento=fumetto).first()
    media_attuale = valutazione.media if valutazione else 0

    template = loader.get_template("Fumetti/fumetto_detail.html")
    context = {
        "fumetto": fumetto,
        "valutazione_attuale": valutazione,
        "media_attuale": media_attuale
    }
    return HttpResponse(template.render(context, request))




def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                login_form.add_error(None, "Credenziali non valide.")
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
        'block_title': "ACCEDI o REGISTRATI",
        'mode': 'login',
    }
    return render(request, "Fumetti/auth.html", context)



def logout_view(request):
    logout(request)
    return redirect('index') 

def register_view(request):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utente creato con successo")
            return redirect('/Fumetti/login/')  
    else:
        form = register_form()
    
    context = {
        'register_form': form,
        'block_title': "ACCEDI o REGISTRATI",
        'mode': 'register'
    }
    return render(request, "Fumetti/auth.html", context)

@login_required
def profile_page_view(request,user_id):
    print("\033[38;5;46m Utente autenticato:", request.user.username, "è entrato nella profile page\033[0m", file=sys.stderr)
    return render(request, "Fumetti/profile_page.html", {})

@login_required
def manga_completato(request, fumetto_id):
    utente_richiesta = User.objects.get(pk = request.user.id)
    profilo = utente_richiesta.profile
    if profilo: 
        
        print(f"\033[240;12;60m Trovato il profilo {profilo}\033[0m")
        if 'id' not in profilo.manga_letti:
            profilo.manga_letti['id'] = []

        if not isinstance(profilo.manga_letti, dict):
            profilo.manga_letti = {}
        if fumetto_id not in profilo.manga_letti['id']:
            profilo.manga_letti['id'].append(fumetto_id)
            print(f"\033[240;12;60m Aggiunto il {fumetto_id} al profilo {profilo}\033[0m")
        else:
            profilo.manga_letti['id'].remove(fumetto_id)
            print(f"\033[31mRimosso il {fumetto_id} al profilo {profilo}\033[0m")

        profilo.save()
        print(profilo.manga_letti)
    return redirect('fumetto_detail', fumetto_id=fumetto_id)