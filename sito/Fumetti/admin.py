# admin.py
from django.contrib import admin
from .models import Artist, Manga, Chapter, Volume, Tab_Generi
from django.contrib.auth.models import User




class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
    fields = ('titolo_capitolo', 'numero_pagine_capitolo', 'data_pubblicazione_capitolo')
    readonly_fields = ('data_pubblicazione_capitolo',)
    show_change_link = True


class VolumeInline(admin.TabularInline):
    model = Volume
    extra = 1
    show_change_link = True



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cognome', 'data_di_nascita')
    search_fields = ('nome', 'cognome')
    
    fieldsets = (
        ('Informazioni Artista', {
            'fields': ('nome', 'cognome', 'data_di_nascita'),
            'description': 'Dati anagrafici dell’artista.'
        }),
    )
    ordering = ('cognome', 'nome')



@admin.register(Tab_Generi)
class GenereAdmin(admin.ModelAdmin):
    list_display = ('nome_genere',)
    search_fields = ('nome_genere',)
    ordering = ('nome_genere',)



@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'artista', 'anno', 'genere')
    list_filter = ('anno', 'genere', 'artista')
    search_fields = ('titolo', 'descrizione', 'artista__nome', 'artista__cognome')
    inlines = [VolumeInline]
    list_per_page = 20

    fieldsets = (
        ('Informazioni Generali', {
            'fields': ('titolo', 'descrizione', 'img_url'),
            'description': 'Titolo e descrizione del manga.'
        }),
        ('Dettagli Editoriali', {
            'fields': ('artista', 'anno', 'genere'),
        }),
    )



@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('fumetto', 'numero')
    list_filter = ('fumetto',)
    search_fields = ('fumetto__titolo',)
    inlines = [ChapterInline]

    fieldsets = (
        ('Informazioni Volume', {
            'fields': ('fumetto', 'numero'),
            'description': 'Collega questo volume al suo manga.'
        }),
    )
    ordering = ('fumetto', 'numero')



@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('titolo_capitolo', 'volume', 'numero_pagine_capitolo', 'data_pubblicazione_capitolo')
    list_filter = ('data_pubblicazione_capitolo', 'volume__fumetto')
    search_fields = ('titolo_capitolo', 'volume__fumetto__titolo')
    date_hierarchy = 'data_pubblicazione_capitolo'
    ordering = ('-data_pubblicazione_capitolo',)

    fieldsets = (
        ('Informazioni Capitolo', {
            'fields': ('titolo_capitolo', 'volume'),
            'description': 'Titolo del capitolo e volume di appartenenza.'
        }),
        ('Dettagli Tecnici', {
            'fields': ('numero_pagine_capitolo', 'data_pubblicazione_capitolo'),
        }),
    )
