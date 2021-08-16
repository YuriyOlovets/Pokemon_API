from django.db import models
from django.contrib.auth.models import User

class Pokemons(models.Model):
    """Pokemon"""
    pokemon_id = models.IntegerField('Pokemon id', unique = True)
    name = models.CharField("Name", max_length=100)
    experience = models.IntegerField('Experience')
    height = models.IntegerField('Height')
    is_default = models.BooleanField('Default?')
    weight = models.IntegerField('Weight')
    owner = models.ManyToManyField(User,blank=True)
    objects = models.Manager()


    def __str__(self):
        return self.name