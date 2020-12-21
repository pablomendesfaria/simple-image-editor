"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import Image


class Negative:
    """
    Classe que ia receber o caminho da imagem da classe MainWindow e ira fazer a transformação e retornar
    a imagem modificada para a MainWindow
    :param parent: é a instancia da MainWindow
    :param path: é o caminho da imagem que esta aberta na aplicação
    """
    def __init__(self, parent, path):
        super(Negative, self).__init__()
        self.main_window = parent
        self.img = Image.open(path)
        self.pixels = list(self.img.getdata())
        self.apply_filter()

    def apply_filter(self):
        """
        Transforma a imagem em negativa substituindo os valores RGB pela subtração deles no valor 255
        retorna a imagem modificada para a classe MainWindow
        """
        for index, pixel in enumerate(self.pixels):
            self.pixels[index] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        self.img.putdata(self.pixels)
        self.main_window.set_image(self.img)
