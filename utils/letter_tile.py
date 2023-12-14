base_letter_values = {
    "?": 0,
    "A": 1,
    "B": 4,
    "C": 4,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 10,
    "K": 5,
    "L": 2,
    "M": 4,
    "N": 2,
    "O": 1,
    "P": 4,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 2,
    "V": 5,
    "W": 4,
    "X": 8,
    "Y": 3,
    "Z": 10,
}


class LetterTile:
    def __init__(self, letter: str):
        self.letter = letter
        self.base_point_value = self._set_base_point_value(letter)

    def _set_base_point_value(self, letter: str):
        return base_letter_values[letter]


class WildcardTile(LetterTile):
    pass
