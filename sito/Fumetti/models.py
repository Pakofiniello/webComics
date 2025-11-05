from django.db import models
from datetime import date, timezone, timedelta

class Tab_Generi(models.Model):
    nome_genere = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome_genere

class Artist(models.Model):
    nome = models.CharField(max_length = 20)
    cognome = models.CharField(max_length = 20)
    data_di_nascita = models.DateField()

    def __str__(self):
        return self.nome +" " + self.cognome

class Manga(models.Model):
    titolo = models.TextField(null = False)
    descrizione = models.TextField()
    artista = models.ForeignKey(Artist, on_delete = models.PROTECT)
    anno = models.IntegerField()
    genere = models.ForeignKey(Tab_Generi, null = True , on_delete=models.SET_NULL)
    img_url = models.TextField(blank = True)
    def __str__(self):
        return self.titolo
    
class Volume(models.Model):
    fumetto = models.ForeignKey(Manga, null = False, on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return f"#{self.numero} - {self.fumetto} "

class Chapter(models.Model):
    titolo_capitolo = models.TextField(max_length=40)
    numero_pagine_capitolo = models.IntegerField()
    data_pubblicazione_capitolo = models.DateField(default=date.today)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        return  self.titolo_capitolo + " - " + self.volume.__str__()
