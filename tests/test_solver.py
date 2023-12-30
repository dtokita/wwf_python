import pytest

from utils.solver import Solver, HighestValueAnagramSolver
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


@pytest.mark.parametrize("tiles, best_word", [("A", "A")])
def test_hvas_find_highest_value_in_hand(tiles, best_word):
    tb = StandardTileBoard()
    th = TileHand()
    bot = StandardBagOfTiles()

    th.tiles = []

    solver = HighestValueAnagramSolver(tb, th, bot)

    solver.find_highest_value_in_hand()
