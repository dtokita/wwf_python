class TileSpace:
    def __init__(self):
        self.current_tile = None
        self.bonus_multiplier = None
        self.is_word_bonus = False
        self.is_tile_bonus = False

    def make_bonus_tile_space(
        self, bonus_multiplier: int, is_word_bonus: bool, is_tile_bonus: bool
    ):
        self.bonus_multiplier = bonus_multiplier
        self.is_word_bonus = is_word_bonus
        self.is_tile_bonus = is_tile_bonus

    def place_tile(self):
        # Check if tile has been placed already
        pass
