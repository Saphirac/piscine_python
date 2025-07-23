from abc import ABC, abstractmethod


class Character(ABC):
    """My abstract character class"""

    @abstractmethod
    def __init__(self, fname, isalive=True):
        """Constructor of my character"""
        super().__init__()
        self.first_name = fname
        self.family_name = self.__class__.__name__
        self.is_alive = isalive

    @abstractmethod
    def die(self):
        """Make a character goes from alive to dead."""
        if self.is_alive:
            self.is_alive = False
        else:
            print(self.first_name, "is already dead.")


class Stark(Character):
    """Class from character of the stark family"""

    def __init__(self, fname, isalive=True):
        """Constructor for the Stark class"""
        super().__init__(fname, isalive)
        self.eyes = "grey"
        self.hairs = "black"

    def die(self):
        """Make the Stark character die."""
        super().die()

