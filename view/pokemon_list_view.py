"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from PyInquirer import prompt, Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.pokemon_details_view import PokemonDetailsView
from view.session import Session
from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        pokemons = PokemonService().get_pokemon_from_webservice(limit=30)
        nomsPokemons =[]
        for pokemon in pokemons:
            nomsPokemons.append({'name' : pokemon.name, 'id':pokemon.id})
        self.__questions = [
            {
                'type': 'list',
                'qmark': '🐹',
                'message': 'Select the pokemon you want to see more detailed',
                'name': 'pokemons',
                'choices': nomsPokemons,
            }
        ]

    def display_info(self):
        print("Hello "+ str(Session().user_name) +", please choose some pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        if answers['pokemons']:
            pokemonSelect = list(filter(lambda q: q['name']==answers['pokemons'], self.__questions[0]['choices']))[0]
            return PokemonDetailsView(pokemonSelect['id'])
        

