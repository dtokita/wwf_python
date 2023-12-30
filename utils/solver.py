from itertools import permutations
from typing import List


from utils.letter_tile import LetterTile
from utils.tile_board import TileBoard
from utils.tile_hand import TileHand
from utils.bag_of_tiles import BagOfTiles
from utils.possible_word import PossibleWord


class Solver:
    def __init__(
        self, tile_board: TileBoard, tile_hand: TileHand, bag_of_tiles: BagOfTiles
    ):
        self.tile_board = tile_board
        self.tile_hand = tile_hand
        self.bag_of_tiles = bag_of_tiles


class HighestValueAnagramSolver(Solver):
    def find_highest_value_in_hand(self):
        wildcard_tiles_idx = [
            i for i, x in enumerate(self.tile_hand.tiles) if x == LetterTile("?")
        ]

        # Check if there are any wildcard tiles in the hand
        if wildcard_tiles_idx:
            highest_value_pw = None
            highest_value = 0

            if len(wildcard_tiles_idx) == 1:
                # There is a single wildcard tile and we iterate over all
                # possible values to find the best combo
                for letter in range(ord("A"), ord("Z") + 1):
                    tiles = list(self.tile_hand.tiles)
                    tiles[wildcard_tiles_idx[0]].set_wildcard_value(chr(letter))

                    _highest_value_pw = self._iterate_through_letter_tiles(tiles)

                    if _highest_value_pw and (
                        _highest_value_pw.base_point_value > highest_value
                    ):
                        highest_value_pw = _highest_value_pw
                        highest_value = _highest_value_pw.base_point_value

            elif len(wildcard_tiles_idx) == 2:
                # There are two wildcard tiles and we iterate over all
                # possible values of those two tiles to find the best combo
                for letter_a in range(ord("A"), ord("Z") + 1):
                    for letter_b in range(ord("A"), ord("Z") + 1):
                        tiles = list(self.tile_hand.tiles)

                        tiles[wildcard_tiles_idx[0]].set_wildcard_value(chr(letter_a))
                        tiles[wildcard_tiles_idx[1]].set_wildcard_value(chr(letter_b))

                        _highest_value_pw = self._iterate_through_letter_tiles(tiles)

                        if _highest_value_pw and (
                            _highest_value_pw.base_point_value > highest_value
                        ):
                            highest_value_pw = _highest_value_pw
                            highest_value = _highest_value_pw.base_point_value
        else:
            highest_value_pw = self._iterate_through_letter_tiles(self.tile_hand.tiles)

        return highest_value_pw

    def _iterate_through_letter_tiles(self, list_of_tiles: List[LetterTile]):
        highest_value_pw = None
        highest_value = 0
        combinations_tried = 0

        for i in range(1, len(list_of_tiles) + 1):
            for tiles in permutations(list_of_tiles, i):
                pw = PossibleWord(tiles)
                combinations_tried += 1

                if pw.is_valid_word and (pw.base_point_value > highest_value):
                    highest_value = pw.base_point_value
                    highest_value_pw = pw

        return highest_value_pw
