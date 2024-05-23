from um import count

def test_um1():
    assert count("um") == 1
    assert count("hellow um") == 1
    assert count("UM hellow Um") == 2
def test_um2():
    assert count(",um,") == 1
    assert count("hellow ,um") == 1
    assert count("UM? hellow .Um..") == 2
def test_um3():
    assert count("yum") == 0
    assert count("hellow ums") == 0
    assert count("UM2 hellow uM") == 1