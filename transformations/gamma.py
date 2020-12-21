"""
Gamma Correction
"""


def correction(parent, pixels, gam):
    """
    Faz a correção gama da imagem de acordo com o valor recebido
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param gam: o valor gamma a ser aplicado nos pixels
    """
    for index, pixel in enumerate(pixels):
        pixels[index] = (int((pixel[0]/255) ** gam * 255),
                         int((pixel[1]/255) ** gam * 255),
                         int((pixel[2]/255) ** gam * 255))
    parent.set_image(pixels)
