"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""


class GrayScale:
    """
    Classe que ia receber o caminho da imagem da classe MainWindow e ira fazer a transformação e retornar
    a imagem modificada para a MainWindow
    :param parent: é a instancia da MainWindow
    :param image: é o caminho da imagem que esta aberta na aplicação
    """
    def __init__(self, parent, image):
        super(GrayScale, self).__init__()
        self.main_window = parent
        self.img = image
        self.pixels = list(self.img.getdata())
        self.apply_filter()

    def apply_filter(self):
        """
        Transforma uma imagem coloria em tons de cinza usando média ponderada, onde o vermelho tem um peso
        de 30%, o verde 59% e o azul 11%, o valor obtido da média bonderada é utilizado no lugar dos valores
        RGB, e a imagem modificada é retornada para a classe MainWindow
        """
        for index, pixel in enumerate(self.pixels):
            average = int((0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2]) / 3)
            self.pixels[index] = (average, average, average)
        self.img.putdata(self.pixels)
        self.main_window.set_image(self.img)
