import pytest

from utils.letter_tile import LetterTile


def test_letter_tile_init():
    lt = LetterTile("A")

    assert lt.letter == "A"
    assert lt.base_point_value == 1


@pytest.mark.parametrize(
    "letter, base_point_value",
    [
        ("A", 1),
        ("B", 4),
        ("C", 4),
        ("D", 2),
        ("E", 1),
        ("F", 4),
        ("G", 3),
        ("H", 3),
        ("I", 1),
        ("J", 10),
        ("K", 5),
        ("L", 2),
        ("M", 4),
        ("N", 2),
        ("O", 1),
        ("P", 4),
        ("Q", 10),
        ("R", 1),
        ("S", 1),
        ("T", 1),
        ("U", 2),
        ("V", 5),
        ("W", 4),
        ("X", 8),
        ("Y", 3),
        ("Z", 10)
    ],
)
def test_letter_tile_base_point_values(letter: str, base_point_value: int):
    lt = LetterTile(letter)

    assert lt.letter == letter
    assert lt.base_point_value == base_point_value
