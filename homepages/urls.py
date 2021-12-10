from django.urls import path
from .views import indexPageView, showPokemonPageView, showSinglePokemonPageView, updatePokemonPageView, deletePokemonPageView, addPokemonPageView

urlpatterns = [
    path("pokemon/", showPokemonPageView, name="pokemon"),
    path("showSinglePokemon/<int:pokemon_id>/", showSinglePokemonPageView, name="showSinglePokemon"),
    path("updatePokemon/", updatePokemonPageView, name="updatePokemon"),
    path("deletePokemon/<int:pokemon_id>", deletePokemonPageView, name="deletePokemon"),
    path("addPokemon/", addPokemonPageView, name="addPokemon"),
    path("", indexPageView, name="index"),
]