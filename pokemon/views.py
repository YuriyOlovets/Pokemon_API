from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.views import View

from .models import *
from django.contrib.auth.models import User


class PokemonList(LoginRequiredMixin,ListView):
    #show all pokemons,exclude-my
    def get_queryset(self):
        pokemons = Pokemons.objects.exclude(owner = self.request.user)
        return pokemons
    paginate_by = 15
    context_object_name = 'pokemon_list'
    login_url = '/account/login/'
    template_name = 'main.html'

def tame_pokemon(request,pk):
    #add pokemon
    pokemon = Pokemons.objects.get(pokemon_id = pk)
    pokemon.owner.add(request.user)
    return redirect('/mypokemons')

class MyPokemons(View):
    #show all my pokemons
    def get(self,request):
        pokemon_list = Pokemons.objects.filter(owner = request.user)
        return render(request,'my_pokemons.html',{'pokemon_list':pokemon_list})

class Players(View):
    #show all user and them pokemons
    def get(self,request):
        players = User.objects.all()
        print(players)
        return render(request,'players.html',{'players':players})