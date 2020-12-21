from PIL import (Image, ImageFilter)


def apply_filter(path):
    img = Image.open(path)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    return img


if __name__ == '__main__':
    apply_filter()
