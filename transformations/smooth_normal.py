from PIL import (Image, ImageFilter)


def apply_filter():
    img = Image.open('sys.argv[1]')
    img = img.filter(ImageFilter.SMOOTH)
    return img


if __name__ == '__main__':
    apply_filter()
