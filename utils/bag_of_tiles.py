import random

from typing import List, Dict, Optional
from collections import defaultdict

from utils.letter_tile import LetterTile
from utils.constants.standard_tile_counts import standard_tile_counts


class BagOfTiles:
    indexed_tiles: Dict[str, List[LetterTile]] = defaultdict(list)
    number_of_tiles = 0

    def __init__(self):
        self._fill_bag()

    def _fill_bag(self) -> None:
        # To be implented in each bag type, needs to fill indexed_tiles
        # and set the number_of_tiles correctly
        pass

    def draw_random_tile(self) -> Optional[LetterTile]:
        # Check if there are any tiles available
        if self.number_of_tiles < 1:
            return None

        drawn_tile = None

        while drawn_tile is None:
            # Choose a random letter
            chosen_letter = random.choice(list(self.indexed_tiles.keys()))

            # Check if there are tiles available for that letter
            if len(self.indexed_tiles[chosen_letter]):
                # Remove the letter from the index and decrement the number_of_tiles
                drawn_tile = self.indexed_tiles[chosen_letter].pop()
                self.number_of_tiles -= 1

                return drawn_tile


class StandardBagOfTiles(BagOfTiles):
    def _fill_bag(self) -> None:
        for letter in standard_tile_counts:
            quantity = standard_tile_counts[letter]

            for _ in range(quantity):
                self.indexed_tiles[letter].append(LetterTile(letter))
                self.number_of_tiles += 1


class UnlimitedBagOfTiles(BagOfTiles):
    pass
