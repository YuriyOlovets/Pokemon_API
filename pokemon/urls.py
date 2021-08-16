from django.urls import path
from . import views


urlpatterns = [    # Обработчики действий со статьями.
    path('', views.PokemonList.as_view() ,name='pokemon'),
    path('mypokemons/', views.MyPokemons.as_view(), name ='my_pokemons'),
    path("tame/<int:pk>/", views.tame_pokemon, name="tame"),
    path("players/", views.Players.as_view(), name="players"),
]