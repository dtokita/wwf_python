from utils.constants.standard_tile_counts import standard_tile_counts

from utils.bag_of_tiles import BagOfTiles, StandardBagOfTiles


def test_bag_of_tiles_init():
    bot = BagOfTiles()

    assert bot.indexed_tiles == {}


def test_standard_bot_fill_bag():
    bot = StandardBagOfTiles()
    total_tiles = 0

    for letter in standard_tile_counts:
        assert len(bot.indexed_tiles[letter]) == standard_tile_counts[letter]

        total_tiles += len(bot.indexed_tiles[letter])

    assert total_tiles == 104
