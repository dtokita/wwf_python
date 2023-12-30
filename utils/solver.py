from itertools import permutations

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
        highest_value_pw = None
        highest_value = 0
        combinations_tried = 0

        for i in range(1, len(self.tile_hand.tiles) + 1):
            for tiles in permutations(self.tile_hand.tiles, i):
                if LetterTile("?") in tiles:
                    for letter in range(ord("A"), ord("Z") + 1):
                        pass

                else:
                    pw = PossibleWord(tiles)
                    combinations_tried += 1

                    if pw.is_valid_word and (pw.base_point_value > highest_value):
                        highest_value = pw.base_point_value
                        highest_value_pw = pw

        return highest_value_pw
