from PyInquirer import Separator, prompt

from view.abstract_view import AbstractView
from view.session import Session
from services.attack_service import AttackService

class AttackDetailsView(AbstractView):
    def __init__(self, idAttaque):
        self.__questions = [
            {
                'type': 'list',
                'name': 'choix',
                'message': 'Bonjour '+str(Session().user_name),
                'choices': [
                     'Attack List'
                    , 'Go back to start menu'

                ]
            }
        ]
        self.__attack = AttackService().get_attack_with_identifier_from_webservice(idAttaque)

    def display_info(self):
        self.__attack.toString()

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse['choix'] == 'Attack List':
            from view.attack_list_view import AttackListView
            return AttackListView()
        elif reponse['choix'] == 'Go back to start menu':
            from view.start_view import StartView
            return StartView()


