"""
Black and White Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma a imagem colorida em preto e branco, ela percorre cada pixel da imagem e verifica se
    a media média dos valores RGB do pixel é menor ou maior do que 128, caso seja menor o pixel RGB
    em questão recebe 0, caso seja maior recebe 255, caso o pixel seja 128 continua 128, depois o
    metodo retorna os pixels modificados para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    for index, pixel in enumerate(pixels):
        average = int((pixel[0] + pixel[1] + pixel[2]) / 3)
        pixels[index] = (0 if average < 128 else 255 if average > 128 else 128,
                         0 if average < 128 else 255 if average > 128 else 128,
                         0 if average < 128 else 255 if average > 128 else 128)
    parent.set_image(pixels, has_filter=True)
