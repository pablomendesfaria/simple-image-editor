import sys
from PIL import Image


def apply_filter():
    img = Image.open(sys.argv[1])
    matrix = img.load()
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            matrix[column, line] = (0, matrix[column, line][1], 0)
    img.save(sys.argv[2])


if __name__ == '__main__':
    apply_filter()
