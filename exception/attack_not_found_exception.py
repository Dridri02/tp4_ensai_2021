class AttackNotFoundException(Exception):
    def __init__(self, identifier):            
        # Call the base class constructor with the parameters it needs
        super().__init__("The attack with the identifier "+str(identifier)+" wasn't found")