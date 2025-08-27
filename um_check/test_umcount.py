from umcount import count


def test_ones():
    assert count("Um, thanks for the album.,") == 1
    assert count("Um, thanks, um...,") == 2
    assert count("um?,") == 1
    assert count("hello, um, world, um.") == 2
def test_zeros():
    assert count("plum") == 0
    assert count("yummy") == 0