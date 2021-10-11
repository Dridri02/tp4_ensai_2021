from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session
from services.pokemon_service import PokemonService

class PokemonDetailsView(AbstractView):
    def __init__(self, idPokemon):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bonjour '+str(Session().user_name),
                'choices': [
                     'Pokemon List'
                    , 'Go back to start menu'

                ]
            }
        ]
        self.__pokemon = PokemonService().get_pokemon_with_identifier_from_webservice(idPokemon)

    def display_info(self):
        print("Description du pokemon choisi : ")
        self.__pokemon.toString()

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Pokemon List':
            from view.pokemon_list_view import PokemonListView
            return PokemonListView()
        elif reponse['choix'] == 'Go back to start menu':
            from view.start_view import StartView
            return StartView()


