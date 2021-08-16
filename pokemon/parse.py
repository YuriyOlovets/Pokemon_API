from .models import *
import pokepy

def pokemon_add(id):
    try:
        pokemon = Pokemons.objects.get(pokemon_id = id)
    except:
        pok = pokepy.V2Client().get_pokemon(id)
        new_pok = Pokemons(pokemon_id=pok[0].id, name=pok[0].name, experience=pok[0].base_experience,
                             height=pok[0].height, is_default=pok[0].is_default, weight=pok[0].weight)
        new_pok.save()
