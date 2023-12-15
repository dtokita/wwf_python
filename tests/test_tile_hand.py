from utils.tile_hand import TileHand


def test_tile_hand_init():
    th = TileHand()

    assert len(th.tiles) == 0
