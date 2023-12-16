from utils.constants.standard_tile_counts import standard_tile_counts

from utils.bag_of_tiles import BagOfTiles, StandardBagOfTiles


def test_bag_of_tiles_init():
    bot = BagOfTiles()

    assert bot.indexed_tiles == {}
    assert bot.number_of_tiles == 0


def test_standard_bot_fill_bag():
    bot = StandardBagOfTiles()

    for letter in standard_tile_counts:
        assert len(bot.indexed_tiles[letter]) == standard_tile_counts[letter]

    assert bot.number_of_tiles == 104


def test_draw_random_tile_empty_bag():
    bot = BagOfTiles()

    # Make sure that the bag is empty
    assert bot.number_of_tiles == 0

    drawn_tile = bot.draw_random_tile()

    # Make sure nothing was drawn from the bag
    assert drawn_tile is None
    assert bot.number_of_tiles == 0


def test_draw_random_tile_full_bag():
    bot = StandardBagOfTiles()

    # Make sure there are tiles in the bag
    initial_number_of_tiles = bot.number_of_tiles
    assert initial_number_of_tiles > 0

    drawn_tile = bot.draw_random_tile()

    # Make sure something was drawn and that the number_of_tiles
    # has been decremented by 1
    assert drawn_tile is not None
    assert (initial_number_of_tiles - 1) == bot.number_of_tiles


def test_draw_random_tile_all_tiles():
    bot = StandardBagOfTiles()

    # Grab the inital number of tiles in the bag
    initial_number_of_tiles = bot.number_of_tiles
    assert initial_number_of_tiles > 0

    # Draw all of the tiles out of the bag
    for _ in range(initial_number_of_tiles):
        drawn_tile = bot.draw_random_tile()

        assert drawn_tile is not None

    # Try to draw another tile
    drawn_tile = bot.draw_random_tile()

    assert drawn_tile is None
    assert bot.number_of_tiles == 0
