class PokemonNotFoundException(Exception):
    def __init__(self, identifier):            
        # Call the base class constructor with the parameters it needs
        super().__init__("The pokemon with the identifier " +str(identifier)+" wasn't found")