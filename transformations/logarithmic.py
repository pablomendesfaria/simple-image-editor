"""
Logarithmic
"""
import math


def log_transform(parent, pixels):
    """
    Faz a transformação logaritmica em uma imagem, usando de uma constante * a operação de log na base 10 do pixel + 1
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    c = 255/math.log(255+1, 10)
    for index, pixel in enumerate(pixels):
        pixels[index] = (c * math.log(pixel[0] + 1, 10),
                         c * math.log(pixel[1] + 1, 10),
                         c * math.log(pixel[2] + 1, 10))
    parent.set_image(pixels, has_filter=True)
