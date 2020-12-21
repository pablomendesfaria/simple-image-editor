from PIL import (Image, ImageFilter)


def apply_filters():
    img = Image.open('original.png')
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    return img


if __name__ == '__main__':
    apply_filters()
