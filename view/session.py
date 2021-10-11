from utils.singleton import Singleton


class Session(metaclass=Singleton):

    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.user_name = "Il faut me renseigner dans la classe Session"
        self.user_mdp = None
        self.listePokemons = []
        self.listeAttaques = []

    def listePokemonsToString(self):
        compteur=1
        print("liste des pokemons en session")
        for pokemon in self.listePokemons:
            print("-----")
            print("POKEMON numéro "+str(compteur))
            pokemon.toString()
            compteur=compteur+1
