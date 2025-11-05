from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Manga, Chapter, Artist, tab_valutazioni
from django.shortcuts import get_object_or_404, redirect
from .forms import LoginForm, register_form
from rest_framework import serializers 
from django.contrib import messages

def index(request):
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

    login_form = LoginForm()
    
    context = {
        'login_form' : login_form,
        'block_title' : "ACCEDI o REGISTRATI",
        'mode' : 'login',
    }
    template = loader.get_template("Fumetti/auth.html")
    return HttpResponse(template.render(context,request))





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



