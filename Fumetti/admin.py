from django.contrib import admin
from .models import Artist, Manga, Chapter, Volume, Tab_Generi

admin.site.register(Artist)
admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Volume)
admin.site.register(Tab_Generi)