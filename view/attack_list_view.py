"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
From : https://github.com/CITGuru/PyInquirer/blob/master/examples/checkbox.py
"""
from pprint import pprint

from PyInquirer import prompt, Separator

from prompt_toolkit.validation import Validator, ValidationError
from view.abstract_view import AbstractView
from view.attack_details import A
from view.session import Session
from client.attack_client import AttackClient


class AttackListView(AbstractView):
    def __init__(self):
        client = AttackClient()
        attaques = client.get_all_attack(limit=30)
        nomsAttaques =[]
        for attaque in attaques:
            nomsAttaques.append({'name' : attaque.name})
        self.__questions = [
            {
                'type': 'checkbox',
                'qmark': '🐹',
                'message': 'Select your Pokemon Team',
                'name': 'pokemons',
                'choices': nomsAttaques,
            }
        ]

    def display_info(self):
        print("Hello "+ str(Session().user_name) +", please choose some pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)
        pprint(answers)
        from view.start_view import StartView
        if reponse['choix']:
            return StartView()
        

