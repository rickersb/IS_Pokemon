from django.urls import path
from .views import detailsPageView, indexPageView, showPokemonPageView, showSinglePokemonPageView, updatePokemonPageView, deletePokemonPageView, addPokemonPageView

urlpatterns = [
    path("<int:pokemon>/", detailsPageView, name="details"),
    path("pokemon/", showPokemonPageView, name="pokemon"),
    path("showPokemon/<int:poke_id>/", showSinglePokemonPageView, name="showSinglePokemon"),
    path("updatePokemon/", updatePokemonPageView, name="updatePoke"),
    path("deletePokemon/<int:poke_id>", deletePokemonPageView, name="deletePokemon"),
    path("addPokemon/", addPokemonPageView, name="addPokemon"),
    path("", indexPageView, name="index"),
]