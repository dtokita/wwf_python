from utils.possible_word import PossibleWord
from utils.letter_tile import LetterTile


def test_possible_word_load_dictionary():
    pw = PossibleWord([])

    assert pw.word_dictionary is not None
    assert len(pw.word_dictionary) == 26


def test_possible_word_init_from_tiles():
    pw = PossibleWord(
        [
            LetterTile("A"),
            LetterTile("P"),
            LetterTile("P"),
            LetterTile("L"),
            LetterTile("E"),
        ]
    )

    assert pw.word == "apple"
    assert pw.base_point_value == 12
    assert pw.is_valid_word


def test_possible_word_not_a_word():
    pw = PossibleWord(
        [
            LetterTile("A"),
            LetterTile("P"),
            LetterTile("P"),
            LetterTile("L"),
            LetterTile("E"),
            LetterTile("Q"),
        ]
    )

    assert pw.word == "appleq"
    assert pw.base_point_value == 22
    assert not pw.is_valid_word
