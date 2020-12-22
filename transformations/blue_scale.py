"""
Blue Scale Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em escala de azul, zerando os valores de vermelho e verde e deixando apenas o azul
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    for index, pixel in enumerate(pixels):
        pixels[index] = (0, 0, pixel[2])
    parent.set_image(pixels, has_filter=True)
