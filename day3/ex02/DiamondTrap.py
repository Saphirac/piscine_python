from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Joffrey Baratheon class"""
    def __init__(self, fname, isalive=True):
        """Creates a King"""
        super().__init__(fname, isalive)
        self.family_name = "Baratheon"
    
    def get_eyes(self):
        """Getter for eyes"""
        return self.eyes
    
    def get_hairs(self):
        """Getter for hairs"""
        return self.hairs
    
    def set_eyes(self, color):
        """Setter for eyes"""
        self.eyes = color
    
    def set_hairs(self, color):
        """Setter for hairs"""
        self.hairs = color

