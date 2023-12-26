from utils.tile_space import TileSpace


def test_tile_board_make_bonus_tile_space():
    ts = TileSpace()

    ts.make_bonus_tile_space(2, True, False)

    assert ts.bonus_multiplier == 2
    assert ts.is_word_bonus
    assert not ts.is_tile_bonus
