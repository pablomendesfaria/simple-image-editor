"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
from PIL import ImageFilter


class Blur:
    """
    Classe que ia receber o caminho da imagem da classe MainWindow e ira fazer a transformação e retornar
    a imagem modificada para a MainWindow
    :param parent: é a instancia da MainWindow
    :param image: é o caminho da imagem que esta aberta na aplicação
    """
    def __init__(self, parent, image):
        super(Blur, self).__init__()
        self.main_window = parent
        self.img = image
        self.pixels = list(self.img.getdata())
        self.apply_filter()

    def apply_filter(self):
        """
        Aplica o filtro Blur na imagem usando a biblioteca PIL e a retorna para a classe MainWindow
        """
        self.img = self.img.filter(ImageFilter.BLUR)
        self.main_window.set_image(self.img)
