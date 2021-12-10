from django.contrib import admin
from .models import PokemonInfo, PokemonType
# Register your models here.

admin.site.register(PokemonInfo)
admin.site.register(PokemonType)