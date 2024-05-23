from project.project import check, apply_filter,convert
from PIL import ImageFilter

def test_check():
    assert check([" "," "," "]) == None
    assert check([" ","invalid.py"]) == None
    assert check(["filter.py", "bridge.bmp"]) != None

def test_convert():
    assert convert("2") == 2
    assert convert("0") == None
    assert convert("11") == None

def test_apply_filter():
    image = check(["filter.py", "bridge.bmp"])
    assert apply_filter(image, 2) == image.filter(ImageFilter.CONTOUR)
    assert apply_filter(image, 10) == image.filter(ImageFilter.SMOOTH_MORE)