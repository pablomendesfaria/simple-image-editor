import sys
from PIL import Image


def apply_filter():
    img_input = Image.open(sys.argv[1])
    img_output = img_input.transpose(Image.ROTATE_180)
    img_output.save(sys.argv[2])


if __name__ == '__main__':
    apply_filter()
