"""
Gray Scale Filter
"""


def apply_filter(parent, pixels):
    """
    Transforma uma imagem coloria em tons de cinza usando média ponderada, onde o vermelho tem um peso
    de 30%, o verde 59% e o azul 11%, o valor obtido da média bonderada é utilizado no lugar dos valores
    RGB, os pixels modificados são retornados para a classe MainWindow
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """
    for index, pixel in enumerate(pixels):
        average = int((0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2]) / 3)
        pixels[index] = (average, average, average)
    parent.set_image(pixels, has_filter=True)
