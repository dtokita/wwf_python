from utils.constants.base_letter_values import base_letter_values


class LetterTile:
    def __init__(self, letter: str):
        self.letter = letter
        self.base_point_value = self._set_base_point_value(letter)

    def _set_base_point_value(self, letter: str):
        return base_letter_values[letter]

    def __repr__(self):
        return f"<LetterTile {self.letter}, {self.base_point_value}>"

    def __eq__(self, other):
        return self.letter == other.letter


class WildcardTile(LetterTile):
    pass
