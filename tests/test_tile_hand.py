from utils.bag_of_tiles import BagOfTiles, StandardBagOfTiles
from utils.letter_tile import LetterTile
from utils.tile_hand import TileHand


def test_tile_hand_init():
    th = TileHand()

    assert len(th.tiles) == 0
    assert th.max_number_of_tiles == 7


def test_tile_hand_fill_hand_from_bag_empty_bag():
    th = TileHand()
    bot = BagOfTiles()  # This bag should be empty

    initial_len_tiles = len(th.tiles)

    th.fill_hand_from_bag(bot)

    # The bag is empty so no new tiles should be added
    assert len(th.tiles) == initial_len_tiles


def test_tile_hand_fill_hand_from_bag_full_bag():
    th = TileHand()
    bot = StandardBagOfTiles()

    assert len(th.tiles) == 0

    th.fill_hand_from_bag(bot)

    # Check that there are exactly the maximum number of tiles
    assert len(th.tiles) == th.max_number_of_tiles


def test_tile_hand_remove_tiles_from_hand_single():
    th = TileHand()

    # Add the "A" tile to the tile hand
    th.tiles.append(LetterTile("A"))

    assert LetterTile("A") in th.tiles

    assert th.remove_tiles_from_hand([LetterTile("A")])

    assert LetterTile("A") not in th.tiles


def test_tile_hand_remove_tiles_from_hand_duplicate():
    th = TileHand()

    # Add the "A" tiles to the tile hand
    th.tiles.append(LetterTile("A"))
    th.tiles.append(LetterTile("A"))

    assert LetterTile("A") in th.tiles
    assert len(th.tiles) == 2

    # Remove one "A" tile
    assert th.remove_tiles_from_hand([LetterTile("A")])

    assert LetterTile("A") in th.tiles
    assert len(th.tiles) == 1

    # Remove one "A" tile
    assert th.remove_tiles_from_hand([LetterTile("A")])

    assert LetterTile("A") not in th.tiles
    assert len(th.tiles) == 0


def test_tile_hand_remove_tiles_from_hand_invalid_tile():
    th = TileHand()

    # Add the "A" tiles to the tile hand
    th.tiles.append(LetterTile("A"))

    # Try to remove one "B" tile
    assert LetterTile("B") not in th.tiles
    assert not th.remove_tiles_from_hand([LetterTile("B")])
    assert len(th.tiles) == 1
    assert LetterTile("A") in th.tiles


def test_tile_hand_exchange_tiles_from_bag_no_tiles_left():
    th = TileHand()
    bot = BagOfTiles()

    assert not th.exchange_tiles_from_bag(th.tiles, bot)


def test_tile_hand_exchange_tiles_from_bag_wrong_tiles():
    th = TileHand()
    bot = StandardBagOfTiles()

    # Draw 7 random tiles, odds are they won't be the same
    # as the tiles in the hand, therefore testing the logic
    # of checking if the exchanged tiles are actually in the
    # hand
    test_tiles = []
    for _ in range(th.max_number_of_tiles):
        test_tiles.append(bot.draw_random_tile())

    assert not th.exchange_tiles_from_bag(test_tiles, bot)


def test_tile_hand_exchange_tiles_from_bag():
    th = TileHand()
    bot = StandardBagOfTiles()

    th.fill_hand_from_bag(bot)

    # Deep copy the inital tiles
    initial_tiles = list(th.tiles)

    assert initial_tiles == th.tiles

    th.exchange_tiles_from_bag(th.tiles, bot)

    assert initial_tiles != th.tiles
