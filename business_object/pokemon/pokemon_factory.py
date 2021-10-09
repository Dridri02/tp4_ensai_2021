from business_object.attack.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.pokemon.speedster_pokemon import SpeedsterPokemon
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic
from business_object.pokemon.supporter_pokemon import SupporterPokemon
from business_object import pokemon
from utils.singleton import Singleton

class PokemonFactory(metaclass=Singleton):
    def instantiate_pokemon(self
                 , type =None
                 , id=None
                 , hp = 0
                 , attack = 0
                 , defense = 0
                 , sp_atk = 0
                 , sp_def = 0
                 , speed = 0
                 , level = 0
                 , name = ""
                 , common_attacks=None):
        if type=="Supporter" :
            pokemon = SupporterPokemon(
                stat_max=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                ,stat_current=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                , id=id
                , level=level
                , name=name
                , common_attacks=common_attacks)
        elif type=="Speedster" :
            pokemon = SpeedsterPokemon(
                stat_max=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                ,stat_current=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                , id=id
                , level=level
                , name=name
                , common_attacks=common_attacks)
        elif type=="Attacker" :
            pokemon = AttackerPokemon(
                stat_max=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                ,stat_current=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                , id=id
                , level=level
                , name=name
                , common_attacks=common_attacks)
        elif type=="Defender" :
            pokemon = DefenderPokemon(
                stat_max=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                ,stat_current=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                , id=id
                , level=level
                , name=name
                , common_attacks=common_attacks)
        elif type=="All-Rounder" :
            pokemon = AllRounderPokemon(
                stat_max=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                ,stat_current=Statistic(
                    hp=hp,
                    attack=attack,
                    defense=defense,
                    sp_atk=sp_atk,
                    sp_def=sp_def,
                    speed=speed
                )
                , id=id
                , level=level
                , name=name
                , common_attacks=common_attacks)
        else :
            raise Exception(str(type)+" n'est pas un type valide")

        return pokemon

