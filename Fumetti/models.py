from django.db import models

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

    def __str__(self):
        return self.titolo
    

class Chapter(models.Model):
    titolo_capitolo = models.TextField(max_length=40)
    fumetto = models.ForeignKey(Manga, on_delete=models.CASCADE)
    numero_pagine_capitolo = models.IntegerField()

    def __str__(self):
        return  self.titolo_capitolo + " - " + self.fumetto.__str__()