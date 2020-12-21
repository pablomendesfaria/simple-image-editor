import sys
from PIL import Image


def apply_filter():
    img = Image.open(sys.argv[1])
    img_png = img.convert('RGBA')
    pixels = list(img_png.getdata())
    for index, pixel in enumerate(pixels):
        pixels[index] = (pixel[0], pixel[1], pixel[2], int(sys.argv[3]))
    img_output = Image.new('RGBA', img.size)
    img_output.putdata(pixels)
    img_output.save(sys.argv[2])


if __name__ == '__main__':
    apply_filter()
