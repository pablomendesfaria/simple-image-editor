"""
Red Scale Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em escala de vermelho, zerando os valores de verde e azul e deixando apenas o vermelho
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    for index, pixel in enumerate(pixels):
        pixels[index] = (pixel[0], 0, 0)
    parent.set_image(pixels)
