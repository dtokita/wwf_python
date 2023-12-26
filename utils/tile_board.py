from typing import List
from utils.tile_space import TileSpace


class TileBoard:
    def __init__(self, num_of_rows: int, num_of_cols: int):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols

        self.board: List[List[TileSpace]] = self._create_blank_board()

    # The first index of the board will be the row
    # number, the second the column number
    #
    # We will also assume that (0, 0) is the bottom left corner of the board
    def _create_blank_board(self) -> List[List[TileSpace]]:
        board = []

        for _ in range(self.num_of_rows):
            row = []

            for _ in range(self.num_of_cols):
                row.append(TileSpace())

            board.append(row)

        return board


class StandardTileBoard(TileBoard):
    # Defined as row_num, col_num, which is inverse x, y
    # coordinates on the plane, assuming 0, 0 is the bottom left
    double_letter_spaces = [
        (1, 2),
        (1, 12),
        (2, 1),
        (2, 4),
        (2, 10),
        (2, 13),
        (4, 2),
        (4, 6),
        (4, 8),
        (4, 12),
        (6, 4),
        (6, 10),
        (8, 4),
        (8, 10),
        (10, 2),
        (10, 6),
        (10, 8),
        (10, 12),
        (12, 1),
        (12, 4),
        (12, 10),
        (12, 13),
        (13, 2),
        (13, 12),
    ]

    triple_letter_spaces = [
        (0, 6),
        (0, 8),
        (3, 3),
        (3, 11),
        (5, 5),
        (5, 9),
        (6, 0),
        (6, 14),
        (8, 0),
        (8, 14),
        (9, 5),
        (9, 9),
        (11, 3),
        (11, 11),
        (14, 6),
        (14, 8),
    ]

    double_word_spaces = [
        (1, 5),
        (1, 9),
        (3, 7),
        (5, 1),
        (5, 13),
        (7, 3),
        (7, 11),
        (9, 1),
        (9, 13),
        (11, 7),
        (13, 5),
        (13, 9),
    ]

    triple_word_spaces = [
        (0, 3),
        (0, 11),
        (3, 0),
        (3, 14),
        (11, 0),
        (11, 14),
        (14, 3),
        (14, 11),
    ]

    def __init__(self):
        super().__init__(15, 15)

        self._create_bonus_spaces()

    def _create_bonus_spaces(self):
        for dl in self.double_letter_spaces:
            self.board[dl[0]][dl[1]].make_bonus_tile_space(2, False, True)

        for tl in self.triple_letter_spaces:
            self.board[tl[0]][tl[1]].make_bonus_tile_space(3, False, True)

        for dw in self.double_word_spaces:
            self.board[dw[0]][dw[1]].make_bonus_tile_space(2, True, False)

        for tw in self.double_word_spaces:
            self.board[tw[0]][tw[1]].make_bonus_tile_space(3, True, False)
