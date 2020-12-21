import sys
from PIL import Image


def apply_transformation():
    img = Image.open(sys.argv[1])
    img = img.convert('RGBA')
    pixels = list(img.getdata())
    message = sys.argv[5]
    message_converted = convert_message(message)
    for index, pixel in enumerate(pixels):
        if index < len(message_converted):
            pixels[index] = (pixel[0], pixel[1], pixel[2], message_converted[index])
        else:
            pixels[index] = (pixel[0], pixel[1], pixel[2], pixel[3])
    img_output = Image.new('RGBA', img.size)
    img_output.putdata(pixels)
    img_output.save(sys.argv[2])


def convert_message(message):
    conversion_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                             "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
                             "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, " ": 27}
    message_converted = []
    for value in message:
        message_converted.append(conversion_dictionary[value])
    return message_converted


if __name__ == '__main__':
    apply_transformation()
