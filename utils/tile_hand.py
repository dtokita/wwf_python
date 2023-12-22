from typing import List

from utils.bag_of_tiles import BagOfTiles
from utils.letter_tile import LetterTile


class TileHand:
    def __init__(self, max_number_of_tiles: int = 7):
        self.tiles: List[LetterTile] = []
        self.max_number_of_tiles = max_number_of_tiles

    def fill_hand_from_bag(self, bag_of_tiles: BagOfTiles) -> None:
        while len(self.tiles) < self.max_number_of_tiles:
            # Check if there are still tiles in the bag
            if bag_of_tiles.number_of_tiles:
                self.tiles.append(bag_of_tiles.draw_random_tile())
            else:
                break  # The bag has no more tiles, break out of the loop

    def remove_tiles_from_hand(self, tiles: List[LetterTile]) -> bool:
        # Check if all of the tiles actually exist in the hand
        for tile in tiles:
            if tile not in self.tiles:
                # Indicate a failed attempt at removing the tiles
                return False

        # Remove the tiles
        for tile in tiles:
            self.tiles.remove(tile)

        # Indicate a successful removal of the tiles
        return True
