from abc import ABC, abstractmethod


class Character(ABC):
    """My abstract character class"""

    @abstractmethod
    def __init__(self, fname, isalive=True):
        """Constructor of my character"""
        super().__init__()
        self.first_name = fname
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

    def die(self):
        """Make the Stark character die."""
        super().die()


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
