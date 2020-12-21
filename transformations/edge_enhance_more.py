"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


def apply_filter(parent, pixels, size):
    """
    Aplica o filtro Edge Enhance More na imagem usando a biblioteca PIL e retorna os pixels da imagem para a classe
    MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param size: tamanho da imagem que recebera o filtro
    """
    img = Image.new('RGBA', size, (255, 255, 255))
    img.putdata(pixels)
    img2 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    parent.set_image(list(img2.getdata()))
