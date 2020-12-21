import sys
from PIL import (Image, ImageFilter)


def apply_filter():
    img_input = Image.open(sys.argv[1])
    img_output = img_input.filter(ImageFilter.SHARPEN)
    img_output.save(sys.argv[2])


if __name__ == '__main__':
    apply_filter()
