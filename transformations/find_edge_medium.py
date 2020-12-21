from PIL import (Image, ImageFilter)


def apply_filters():
    kernel = ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1)
    img = Image.open('original.png')
    img = img.filter(kernel)
    return img


if __name__ == '__main__':
    apply_filters()
