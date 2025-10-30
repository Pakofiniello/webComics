from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Manga, Chapter, Artist
from django.shortcuts import get_object_or_404
from .forms import LoginForm, register_form

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
    fumetto = get_object_or_404(Manga, id = fumetto_id)
    template = loader.get_template("Fumetti/fumetto_detail.html")
    context = {"fumetto":fumetto}
    return HttpResponse(template.render(context,request))

def login_view(request):

    login_form = LoginForm()
    
    context = {
        'login_form' : login_form,
        'block_title' : "ACCEDI o REGISTRATI",
    }
    template = loader.get_template("Fumetti/auth.html")
    return HttpResponse(template.render(context,request))


    
    