from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session
from client.pokemon_client import PokemonClient


class PokemonDetailsView(AbstractView):
    def __init__(self, idPokemon):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bonjour '+str(Session().user_name),
                'choices': [
                     'Pokemon List'
                    , 'Attack List'
                    , 'Go back to start menu'

                ]
            }
        ]
        client = PokemonClient()
        self.__pokemon = client.get_pokemon(idPokemon)

    def display_info(self):
        self.__pokemon.toString()

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Pokemon List':
            from view.pokemon_list_view import PokemonListView
            return PokemonListView()
        elif reponse['choix'] == 'Attack List':
            from view.attack_list_view import AttackListView
            return AttackListView()
        elif reponse['choix'] == 'Go back to start menu':
            from view.start_view import StartView
            return StartView()


