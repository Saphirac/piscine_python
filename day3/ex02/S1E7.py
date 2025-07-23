from S1E9 import Character

class Baratheon(Character):
    """Class from character of the baratheon family"""
    def __init__(self, fname, isalive=True):
        """Constructor for the baratheon class"""
        super().__init__(fname, isalive)
        self.eyes = "brown"
        self.hairs = "dark"
    
    def die(self):
        """Make the Baratheon character die."""
        super().die()

    def __str__(self):
        """Str method for baratheon"""
        return f"{self.first_name} : {self.is_alive}"
    
    def __repr__(self):
        """Repr method for baratheon"""
        return f"Baratheon object inheriting from class Character : {self.first_name};{self.is_alive}"

class Lannister(Character):
    """Class from character of the Lannister family"""
    def __init__(self, fname, isalive=True):
        """Constructor for the Lannister class"""
        super().__init__(fname, isalive)
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self):
        """Make the Lannister character die."""
        super().die()

    def __str__(self):
        """Str method for lannister"""
        return f"{self.first_name} : {self.is_alive}"
    
    def __repr__(self):
        """Repr method for lannister"""
        return f"Lannister object inheriting from class Character : {self.first_name};{self.is_alive}"
        
    @classmethod
    def create_lannister(cls, fname, isalive=True):
        """Class method to create lannister"""
        return cls(fname, isalive)

