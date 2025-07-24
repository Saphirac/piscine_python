import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function to randomly generate an id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


# dataclass is a decorator that automatically creates an __init__ method for the class you call it on


@dataclass
class Student:
    """My Student class"""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Will be called after the init method"""
        self.login = f"{self.name[0]}{self.surname[:7]}"


def main():
    student = Student(name="Edward", surname="agle")
    print(student)

    student2 = Student("John", "Dowefwefwefwee")
    print(student2)


if __name__ == "__main__":
    main()

# student3 = Student(name = "Edward", surname = "agle", id = "toto")
# print(student)
