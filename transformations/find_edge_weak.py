"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import (Image, ImageFilter)


def apply_filter(parent, pixels, size):
    """
    Aplica o filtro Find Edge Weak a partir de um kernel pre estabelecido e retorna os pixels da imagem para a classe
    MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param size: tamanho da imagem que recebera o filtro
    """
    kernel = ImageFilter.Kernel((3, 3), (1, 0, -1, 0, 0, 0, -1, 0, 1), 1)
    img = Image.new('RGB', size, (255, 255, 255))
    img.putdata(pixels)
    img2 = img.filter(kernel)
    parent.set_image(list(img2.getdata()))
