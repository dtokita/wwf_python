from utils.tile_space import TileSpace


class TileBoard:
    def __init__(self, num_of_rows: int, num_of_cols: int):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols

        self.board = self._create_blank_board()

    # The first index of the board will be the row
    # number, the second the column number
    def _create_blank_board(self):
        board = []

        for _ in range(self.num_of_rows):
            row = []

            for _ in range(self.num_of_cols):
                row.append(TileSpace())

            board.append(row)

        return board


class StandardTileBoard(TileBoard):
    pass
