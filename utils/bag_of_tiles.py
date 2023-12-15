from typing import List, Dict
from collections import defaultdict

from utils.letter_tile import LetterTile
from utils.constants.standard_tile_counts import standard_tile_counts


class BagOfTiles:
    indexed_tiles: Dict[str, List[LetterTile]] = defaultdict(list)

    def __init__(self):
        self._fill_bag()

    def _fill_bag(self):
        # To be implented in each bag type
        pass


class StandardBagOfTiles(BagOfTiles):
    def _fill_bag(self):
        for letter in standard_tile_counts:
            quantity = standard_tile_counts[letter]

            for _ in range(quantity):
                self.indexed_tiles[letter].append(LetterTile(letter))


class UnlimitedBagOfTiles(BagOfTiles):
    pass
