from utils.tile_space import TileSpace
from utils.letter_tile import LetterTile


def test_tile_space_make_bonus_tile_space():
    ts = TileSpace()

    ts.make_bonus_tile_space(2, True, False)

    assert ts.bonus_multiplier == 2
    assert ts.is_word_bonus
    assert not ts.is_tile_bonus


def test_tile_space_place_letter_tile_on_tile_space():
    ts = TileSpace()
    tl = LetterTile("A")

    assert ts.place_letter_tile_on_tile_space(tl)


def test_tile_space_place_letter_tile_on_occupied_tile_space():
    ts = TileSpace()
    tl = LetterTile("A")

    assert ts.place_letter_tile_on_tile_space(tl)
    assert not ts.place_letter_tile_on_tile_space(tl)
