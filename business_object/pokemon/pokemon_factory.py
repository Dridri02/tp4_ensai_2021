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
                 , common_attacks=None
        """
        Instantiate a Pokemon of the good type based on the
        type argument. The method is pretty ugly, but it's only to
        instantiate pokemon, so it's ok.

        :param type: the type of the pokemon
        :type type: str
        :param hp: the hp (current and max) of the pokemon defaults to 0
        :type hp: int, optional
        :param attack: the attack (current and max) of the pokemon, defaults to 0
        :type attack: int, optional
        :param defense: the defense (current and max) of the pokemon, defaults to 0
        :type defense: int, optional
        :param sp_atk: the sp_atk (current and max) of the pokemon, defaults to 0
        :type sp_atk: int, optional
        :param sp_def: the sp_def (current and max) of the pokemon, defaults to 0
        :type sp_def: int, optional
        :param speed: the speed (current and max) of the pokemon, defaults to 0
        :type speed: int, optional
        :param level: the level of the pokemon, defaults to None
        :type level: int, optional
        :param name: the pokemon name, defaults to None
        :type name: str, optional
        :param common_attacks: the list of the pokemon's attack, defaults to []
        :type common_attacks: list, optional
        :raises Exception: if the type is unknown, an exception is raised
        """

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

