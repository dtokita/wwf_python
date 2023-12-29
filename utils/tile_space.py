from utils.letter_tile import LetterTile


class TileSpace:
    def __init__(self):
        self.current_tile = None
        self.bonus_multiplier = None
        self.is_word_bonus = False
        self.is_tile_bonus = False
        self.is_starting_space = False

    def make_bonus_tile_space(
        self, bonus_multiplier: int, is_word_bonus: bool, is_tile_bonus: bool
    ):
        self.bonus_multiplier = bonus_multiplier
        self.is_word_bonus = is_word_bonus
        self.is_tile_bonus = is_tile_bonus

    def make_starting_tile_space(self):
        self.is_starting_space = True

    def place_letter_tile_on_tile_space(self, letter_tile: LetterTile) -> bool:
        if not self.current_tile:
            self.current_tile = letter_tile

            return True

        return False
