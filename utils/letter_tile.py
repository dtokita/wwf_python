from utils.constants.base_letter_values import base_letter_values


class LetterTile:
    def __init__(self, letter: str):
        if letter == "?":
            self.is_wildcard = True
        else:
            self.is_wildcard = False

        self.letter = letter
        self.base_point_value = self._set_base_point_value(letter)

    def _set_base_point_value(self, letter: str):
        return base_letter_values[letter]

    def set_wildcard_value(self, letter: str) -> bool:
        if self.is_wildcard:
            self.letter = letter

            return True

        return False

    def __repr__(self):
        return f"<LetterTile {self.letter}, {self.base_point_value}>"

    def __eq__(self, other):
        return self.letter == other.letter


class WildcardTile(LetterTile):
    pass
