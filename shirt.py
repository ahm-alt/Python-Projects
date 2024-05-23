from sys import exit, argv
from PIL import Image, ImageOps

def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    if len(argv) > 3:
        exit("Too many command-line arguments")
    if (".jpg" not in argv[1] or ".jpg" not in argv[2]) and (".jpeg" not in argv[1] or ".jpeg" not in argv[2]) and (".png" not in argv[1] or ".png" not in argv[2]):
        exit("invalid input")
    try:
        image = Image.open(argv[1])
    except FileNotFoundError:
        exit("Could not read")
    shirt = Image.open("shirt.png")
    size = shirt.size
    image.save("b.jpg")
    image = ImageOps.fit(image, size)
    image.save("a.jpg")
    image.paste(shirt, shirt)
    #photo.paste(shirt, shirt)
    image.save(argv[2])

main()