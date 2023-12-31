import pytest

from utils.solver import Solver, HighestValueAnagramSolver
from utils.letter_tile import LetterTile
from utils.tile_board import StandardTileBoard
from utils.tile_hand import TileHand
from utils.bag_of_tiles import BagOfTiles, StandardBagOfTiles


def test_solver_init():
    tb = StandardTileBoard()
    th = TileHand()
    bot = BagOfTiles()

    solver = Solver(tb, th, bot)

    assert solver.tile_board == tb
    assert solver.tile_hand == th
    assert solver.bag_of_tiles == bot


@pytest.mark.parametrize(
    "tiles, best_words",
    [
        ("ABCDEFG", ["decaf", "faced"]),
        ("HIJKLMN", ["jink"]),
        ("OPQRSTU", ["suq"]),
        ("VWXYZZ?", ["zax"]),
        ("VWXYZ??", ["zax"]),
        ("??AEIOU", ["eulogia", "miaoued", "sequoia"]),
        ("QWERTY", ["qwerty"]),
    ],
)
def test_hvas_find_highest_value_in_hand(tiles, best_words):
    tb = StandardTileBoard()
    th = TileHand()
    bot = StandardBagOfTiles()

    for letter in tiles:
        th.tiles.append(LetterTile(letter))

    solver = HighestValueAnagramSolver(tb, th, bot)

    highest_value_pw = solver.find_highest_value_in_hand()

    assert highest_value_pw.word in best_words
