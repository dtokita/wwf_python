from typing import List

from utils.constants.dictionary import dictionary
from utils.letter_tile import LetterTile


class PossibleWord:
    word_dictionary = dictionary

    def __init__(self, tiles: List[LetterTile]):
        self.tiles = tiles
        self.word = ""
        self.base_point_value = 0

        for tile in tiles:
            self.word += tile.letter.lower()
            self.base_point_value += tile.base_point_value

        self.is_valid_word = self._is_valid_word()

    def _is_valid_word(self) -> bool:
        # A word must be at least two letters long
        if len(self.tiles) < 2:
            return False

        # Attempt to look it up in the dictionary
        word_list_by_len = self.word_dictionary[str(len(self.tiles))]

        if word_list_by_len.get(self.word[:2]):
            return self.word in word_list_by_len[self.word[:2]]

    def __repr__(self):
        return f"<PossibleWord {self.word}, {self.base_point_value}>"
