from sys import exit, argv
from PIL import Image, ImageFilter

filters={
        1:"BLUR",
        2:"CONTOUR",
        3:"DETAIL",
        4:"EDGE_ENHANCE",
        5:"EDGE_ENHANCE_MORE",
        6:"EMBOSS",
        7:"FIND_EDGES",
        8:"SHARPEN",
        9:"SMOOTH",
        10:"SMOOTH_MORE"
    }
def main():

    image = check(argv)
    if not image:
        exit("you should provide image file")

    for i in range(10):
        print(f"{i+1} - {filters[i+1]}")
    n = input("Inter index of filter that you want to apply to image ")
    filter = convert(n)
    if not filter:
        exit("you should enter a valid number")

    new_image = apply_filter(image, filter)
    new_image.save("out.bmp")

def check(files):
    if len(files) != 2 :
        return None
    try:
        return Image.open(files[1])
    except FileNotFoundError:
        return None

def convert(n):
    try:
        n = int(n)
        if 1 <= n <= 10:
            return n
    except ValueError:
            return None
def apply_filter(im, filter):
    if filter == 1:
        return im.filter(ImageFilter.BLUR)
    elif filter == 2:
        return im.filter(ImageFilter.CONTOUR)
    elif filter == 3:
        return im.filter(ImageFilter.DETAIL)
    elif filter == 4:
        return im.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == 5:
        return im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == 6:
        return im.filter(ImageFilter.EMBOSS)
    elif filter == 7:
        return im.filter(ImageFilter.FIND_EDGES)
    elif filter == 8:
        return im.filter(ImageFilter.SHARPEN)
    elif filter == 9:
        return im.filter(ImageFilter.SMOOTH)
    else:
        return im.filter(ImageFilter.SMOOTH_MORE)

def se(n):
    return n
if __name__ == "__main__":
    main()



