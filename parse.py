from pokemon import models
import pokepy

pok = pokepy.V2Client().get_pokemon(14)
new_pok = models.Pokemons(pokemon_id = pok[0].id,name = pol[0].name,experience = pol[0].base_experiance,height = pol[0].height,is_default = pol[0].is_default,weight = pol[0].weight)
new_pok.save()