import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": "...-",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def main():
    """Morse code converter"""
    assert len(sys.argv) == 2
    assert all(c.isalnum() or c.isspace() for c in sys.argv[1])
    print(
        " ".join(
            [NESTED_MORSE[c.upper()] for c in sys.argv[1] if c.isalnum() or c == " "]
        )
    )


if __name__ == "__main__":
    sys.tracebacklimit = 0
    try:
        main()
    except AssertionError as e:
        print(f"{e.__class__.__name__}: the arguments are bad")
