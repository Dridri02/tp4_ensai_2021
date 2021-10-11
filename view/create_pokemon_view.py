from pprint import pprint
from prompt_toolkit.validation import ValidationError, Validator
from PyInquirer import  prompt

from view.abstract_view import AbstractView
from view.session import Session
from business_object.pokemon.pokemon_factory import PokemonFactory

class CreatePokemonView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [
            {
                'type': 'input',
                'name': 'pokemon_name',
                'message': 'What\'s the pokemon name',
            },
            {
                'type': 'input',
                'name': 'pokemon_hp',
                'message': 'What\'s the pokemon hp',
            }
        ]

    def display_info(self):
        print("Hello "+ str(Session().user_name) +", you can create pokemons here")
        print(" the pokemons created and stored in session are :")
        Session().listePokemonsToString()

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        #j'ai fait la correction en remplissant seulement name et hp, pour chaque autre caractéristique/attribut le fonctionnement
        # est similaire
        if(answers["pokemon_name"] and answers["pokemon_hp"]):
            newPokemon = PokemonFactory().instantiate_pokemon(
                  type ="Speedster"
                 , id=None
                 , hp = answers["pokemon_hp"]
                 , attack = 0
                 , defense = 0
                 , sp_atk = 0
                 , sp_def = 0
                 , speed = 0
                 , level = 0
                 , name = answers["pokemon_name"]
                 )
            Session().listePokemons.append(newPokemon)
            Session().listePokemonsToString()
            from view.start_view import StartView
            return StartView()
            

        
        
