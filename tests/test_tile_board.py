from utils.tile_board import TileBoard, StandardTileBoard
from utils.tile_space import TileSpace


def test_tile_board_create_blank_board():
    tb = TileBoard(3, 4)

    assert tb.num_of_rows == 3
    assert tb.num_of_cols == 4
    assert len(tb.board) == 3
    assert len(tb.board[0]) == 4
    assert isinstance(tb.board[0][0], TileSpace)


def test_standard_tile_board_init():
    tb = StandardTileBoard()

    assert tb.num_of_rows == 15
    assert tb.num_of_cols == 15
    assert len(tb.board) == 15
    assert len(tb.board[0]) == 15
