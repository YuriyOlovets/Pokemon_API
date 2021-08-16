from django.contrib import admin
from django.urls import path,include
from pokemon import parse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pokemon.urls')),
    path('account/',include('account.urls')),
]
for i in range(1,200): #run when runserver
    parse.pokemon_add(i)