from django.db import models

    
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
        return self.fumetto + "#" + self.numero

class Chapter(models.Model):
    numero_capitolo = models.IntegerField(blank = True)
    titolo_capitolo = models.TextField(max_length=40)
    fumetto = models.ForeignKey(Manga, on_delete=models.CASCADE)
    numero_pagine_capitolo = models.IntegerField()

    def __str__(self):
        return  self.titolo_capitolo + " - " + self.fumetto.__str__()
