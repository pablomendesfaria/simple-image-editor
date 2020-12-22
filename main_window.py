"""
Faz a importação das classes necessarias da biblioteca PyQt5
"""
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from PyQt5.QtCore import (QObject, Qt, QDir)
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtWidgets import (QDialog, QLabel, QMainWindow, QAction, QSlider, QDoubleSpinBox, QSpinBox, QPushButton,
                             QFileDialog, QApplication, QInputDialog)
from transformations import (black_and_white, blur, countor, detail, edge_enhance_normal, edge_enhance_more, emboss,
                             find_edge_weak, find_edge_medium, find_edge_strong, flip_horizontally, flip_vertically,
                             gray_scale, hide_message, identify_message, negative, rotate_270, red_scale,
                             green_scale, blue_scale, sharpen, smooth_normal, smooth_more, transparency, gamma)


class AboutAppDialog(QDialog):
    """
    Classe que representa o dialogo para mostrar as informações sobre o app
    Carrega o arquivo .ui que contem a interface grafica
    """
    def __init__(self):
        super(AboutAppDialog, self).__init__()
        uic.loadUi('about_app_dialog.ui', self)


class AboutImageDialog(QDialog):
    """
    Classe que representa o dialogo para mostrar as informações sobre a imagem
    Carrega o arquivo .ui que contem a interface grafica e em seguida atualiza os labels name, type, comment
    width e height com os devidos parametros recebidos da classe MainWindow
    :param name: é o nome do arquivo da imagem
    :param type: é o o tipo de arquivo (extensão) da imagem
    :param comment: não sei
    :param width: é a largura da imagem
    :param height: é a altura da imagem
    """
    def __init__(self, name, type, comment, width, height):
        super(AboutImageDialog, self).__init__()
        uic.loadUi('about_image_dialog.ui', self)
        self.name = self.findChild(QLabel, 'nameLabel')
        self.type = self.findChild(QLabel, 'typeLabel')
        self.comment = self.findChild(QLabel, 'commentLabel')
        self.width = self.findChild(QLabel, 'widthLabel')
        self.height = self.findChild(QLabel, 'heightLabel')
        self.name.setText(name)
        self.type.setText(type)
        self.comment.setText(comment)
        self.width.setText(width)
        self.height.setText(height)


class SecretDialog(QDialog):
    """
    Classe que representa o dialogo para mostrar na tela a mensagem secreta que foi descoberta na imagem
    Carrega o arquivo .ui que contem a interface grafica e em seguida atualiza o label com a mensagem secreta
    recebida como parametro da classe MainWindow
    :param self: é a propria janela de dialogo
    :param message: é a mensagem secreta
    """
    def __init__(self, message):
        super(SecretDialog, self).__init__()
        uic.loadUi('secret_dialog.ui', self)
        self.secret_message = self.findChild(QLabel, 'secretLabel')
        self.decrypt_message = self.findChild(QLabel, 'decryptLabel')
        self.btn_ok = self.findChild(QPushButton, 'btnOk')
        self.btn_decrypt = self.findChild(QPushButton, 'btnDecrypt')

        self.message = message

        self.setup_ui()

    def setup_ui(self):
        """
        Define as interações da aplicação, o que cada botão faz ao ser clicado e etc.
        """
        self.btn_ok.clicked.connect(self.accept)
        self.secret_message.setText(self.message)


class MainWindow(QMainWindow):
    """
    Classe que representa a janela principal da aplicação
    Carrega um arquivo .ui que contem toda a interface principal
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.status_bar = self.findChild(QObject, 'statusBar')

        self.action_open = self.findChild(QAction, 'actionOpen')
        self.action_save = self.findChild(QAction, 'actionSave')
        self.action_save_as = self.findChild(QAction, 'actionSave_As')
        self.action_exit = self.findChild(QAction, 'actionExit')

        self.action_black_and_white = self.findChild(QAction, 'actionBlack_and_White')
        self.action_gray_scale = self.findChild(QAction, 'actionGray_Scale')
        self.action_negative = self.findChild(QAction, 'actionNegative')
        self.action_blur = self.findChild(QAction, 'actionBlur')
        self.action_countor = self.findChild(QAction, 'actionCountor')
        self.action_detail = self.findChild(QAction, 'actionDetail')
        self.action_e_e_normal = self.findChild(QAction, 'actionE_E_Normal')
        self.action_e_e_more = self.findChild(QAction, 'actionE_E_More')
        self.action_emboss = self.findChild(QAction, 'actionEmboss')
        self.action_f_e_weak_detection = self.findChild(QAction, 'actionF_E_Weak_Detection')
        self.action_f_e_medium_detection = self.findChild(QAction, 'actionF_E_Medium_Detection')
        self.action_f_e_strong_detection = self.findChild(QAction, 'actionF_E_Strong_Detection')
        self.action_sharpen = self.findChild(QAction, 'actionSharpen')
        self.action_s_normal = self.findChild(QAction, 'actionS_Normal')
        self.action_s_more = self.findChild(QAction, 'actionS_More')
        self.action_red_scale = self.findChild(QAction, 'actionRed_Scale')
        self.action_green_scale = self.findChild(QAction, 'actionGreen_Scale')
        self.action_blue_scale = self.findChild(QAction, 'actionBlue_Scale')

        self.action_hide_text = self.findChild(QAction, 'actionHide_Text')
        self.action_identify_secret_text = self.findChild(QAction, 'actionIdentify_Secret_Text')

        self.action_about_app = self.findChild(QAction, 'actionAbout_App')
        self.action_about_image = self.findChild(QAction, 'actionAbout_Img')

        self.open_image_label = self.findChild(QLabel, 'openImageLabel')
        self.image_label = self.findChild(QLabel, 'imageLabel')

        self.gamma_slider = self.findChild(QSlider, 'gammaSlider')
        self.transparency_slider = self.findChild(QSlider, 'transpaSlider')

        self.gamma_spin = self.findChild(QDoubleSpinBox, 'gammaSpin')
        self.transparency_spin = self.findChild(QSpinBox, 'transpaSpin')

        self.btn_rotate = self.findChild(QPushButton, 'btnRotate')
        self.btn_flip_h = self.findChild(QPushButton, 'btnFlipH')
        self.btn_flip_v = self.findChild(QPushButton, 'btnFlipV')
        self.btn_reset = self.findChild(QPushButton, 'btnReset')

        self.file_name = QLabel('Name: No file open   ')
        self.file_name.setStyleSheet('color: rgb(231, 34, 88)')
        self.file_path = QLabel('   Path: No file open   ')
        self.file_path.setStyleSheet('color: rgb(231, 34, 88)')
        self.save_status = QLabel('   Save Status: No file open   ')
        self.save_status.setStyleSheet('color: rgb(231, 34, 88)')

        self.img_path = ' '
        self.image = None
        self.pixels_bkup = []
        self.transform_bkup = []
        self.pixels = []
        self.has_filter = False
        self.setup_status_bar()
        self.setup_ui()

    def setup_status_bar(self):
        """
        Adiciona os label que contem o nome, local do arquivo e status de salvamento na barra de status
        """
        self.status_bar.addPermanentWidget(self.file_name)
        self.status_bar.addPermanentWidget(self.file_path)
        self.status_bar.addPermanentWidget(self.save_status)

    def setup_ui(self):
        """
        Define as interações da aplicação, o que cada botão faz ao ser clicado e etc.
        """
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save)
        self.action_save_as.triggered.connect(self.save_as)
        self.action_exit.triggered.connect(sys.exit)

        self.action_about_app.triggered.connect(about_app_dialog)
        self.action_about_image.triggered.connect(self.about_image_dialog)

        self.action_black_and_white.triggered.connect(lambda: black_and_white.apply_filter(self, self.pixels))
        self.action_gray_scale.triggered.connect(lambda: gray_scale.apply_filter(self, self.pixels))
        self.action_negative.triggered.connect(lambda: negative.apply_filter(self, self.pixels))
        self.action_blur.triggered.connect(lambda: blur.apply_filter(self, self.pixels, self.image.size))
        self.action_countor.triggered.connect(lambda: countor.apply_filter(self, self.pixels, self.image.size))
        self.action_detail.triggered.connect(lambda: detail.apply_filter(self, self.pixels, self.image.size))
        self.action_e_e_normal.triggered.connect(lambda: edge_enhance_normal.apply_filter(self, self.pixels,
                                                                                          self.image.size))
        self.action_e_e_more.triggered.connect(lambda: edge_enhance_more.apply_filter(self, self.pixels,
                                                                                      self.image.size))
        self.action_emboss.triggered.connect(lambda: emboss.apply_filter(self, self.pixels, self.image.size))
        self.action_f_e_weak_detection.triggered.connect(lambda: find_edge_weak.apply_filter(self, self.pixels,
                                                                                             self.image.size))
        self.action_f_e_medium_detection.triggered.connect(lambda: find_edge_medium.apply_filter(self, self.pixels,
                                                                                                 self.image.size))
        self.action_f_e_strong_detection.triggered.connect(lambda: find_edge_strong.apply_filter(self, self.pixels,
                                                                                                 self.image.size))
        self.action_sharpen.triggered.connect(lambda: sharpen.apply_filter(self, self.pixels, self.image.size))
        self.action_s_normal.triggered.connect(lambda: smooth_normal.apply_filter(self, self.pixels, self.image.size))
        self.action_s_more.triggered.connect(lambda: smooth_more.apply_filter(self, self.pixels, self.image.size))
        self.action_red_scale.triggered.connect(lambda: red_scale.apply_filter(self, self.pixels))
        self.action_green_scale.triggered.connect(lambda: green_scale.apply_filter(self, self.pixels))
        self.action_blue_scale.triggered.connect(lambda: blue_scale.apply_filter(self, self.pixels))

        self.action_hide_text.triggered.connect(self.hide_text_dialog)
        self.action_identify_secret_text.triggered.connect(lambda: identify_message.find_message(self.pixels))

        self.btn_rotate.clicked.connect(lambda: rotate_270.rotate(self, self.pixels, self.image.size))
        self.btn_flip_h.clicked.connect(lambda: flip_horizontally.flip(self, self.pixels, self.image.size))
        self.btn_flip_v.clicked.connect(lambda: flip_vertically.flip(self, self.pixels, self.image.size))
        self.btn_reset.clicked.connect(self.reset)

        self.gamma_slider.valueChanged[int].connect(self.gamma_correction)
        self.transparency_slider.valueChanged[int].connect(self.change_tansparency)

    def open_file(self):
        """
        Abre uma imagem escolhida pelo usuario e define o label image como sendo essa imagem mantendo as proporções
        da imagem, tambem define a variavel image que sera a imagem usada para as transformações como sendo a imagem
        aberta, assim como tambem o seu back up caso o usuario queira resetar.
        """
        path, _ = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                     'Images (*.png; *.jpg)', 'Images '
                                                                                                              '(*.png'
                                                                                                              '; '
                                                                                                              '*.jpg)')
        self.img_path = path
        self.set_enable_disable()

    def save(self):
        """
        Salva a imagem no caminho de destino com o mesmo nome, assim sobreescrevendo a antiga
        """
        self.image.save(self.img_path)
        self.save_status.setText('   Save Status: Saved   ')

    def save_as(self):
        """
        Salva a imagem com o nome, local e tipo de arquivo definido pelo usuario
        """
        path, _ = QFileDialog.getSaveFileName(self, 'Save File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                     'Images (*.png)', 'Images '
                                                                                                       '(*.png')
        self.img_path = path
        self.image.save(self.img_path)
        self.set_up_image()
        self.file_name.setText(f'   Name: {self.get_image_name()}   ')
        self.file_path.setText(f'   Path: {self.img_path}   ')
        self.save_status.setText('   Save Status: Saved   ')
        self.action_save.setEnabled(True)

    def about_image_dialog(self):
        """
        Inicia o dialogo que contem as informações da imagem
        """
        name = self.get_image_name()
        type = self.image.format
        comment = 'lol'
        width, height = self.image.size
        image_dialog = AboutImageDialog(name[0], type, comment, str(width), str(height))
        image_dialog.exec_()

    def set_enable_disable(self):
        """
        Apos uma imagem ser aberta os componentes que estavam desabilitados seram ativados e outros que estavam ativados
        desabilitados
        """
        self.action_save.setEnabled(False)
        self.action_save_as.setEnabled(True)

        self.action_black_and_white.setEnabled(True)
        self.action_gray_scale.setEnabled(True)
        self.action_negative.setEnabled(True)
        self.action_blur.setEnabled(True)
        self.action_countor.setEnabled(True)
        self.action_detail.setEnabled(True)
        self.action_e_e_normal.setEnabled(True)
        self.action_e_e_more.setEnabled(True)
        self.action_emboss.setEnabled(True)
        self.action_f_e_weak_detection.setEnabled(True)
        self.action_f_e_medium_detection.setEnabled(True)
        self.action_f_e_strong_detection.setEnabled(True)
        self.action_sharpen.setEnabled(True)
        self.action_s_normal.setEnabled(True)
        self.action_s_more.setEnabled(True)
        self.action_red_scale.setEnabled(True)
        self.action_green_scale.setEnabled(True)
        self.action_blue_scale.setEnabled(True)

        self.action_hide_text.setEnabled(True)
        self.action_identify_secret_text.setEnabled(True)

        self.action_about_image.setEnabled(True)

        self.open_image_label.setDisabled(True)
        self.open_image_label.setVisible(False)

        self.gamma_slider.setEnabled(True)
        self.transparency_slider.setEnabled(True)

        self.btn_rotate.setEnabled(True)
        self.btn_flip_h.setEnabled(True)
        self.btn_flip_v.setEnabled(True)
        self.btn_reset.setEnabled(True)

        img = Image.open(self.img_path)
        img = img.convert('RGBA')
        self.pixels = list(img.getdata().copy())
        self.image = img.copy()
        self.pixels_bkup = list(img.getdata().copy())
        self.verify_rotate_or_square()

        self.file_name.setText(f'   Name: {self.get_image_name()}   ')
        self.file_path.setText(f'   Path: {self.img_path}   ')
        self.save_status.setText('   Sava Status: Without Changes   ')

    def get_image_name(self):
        """
        Pega o nome da imagem na string que contrem o caminho completa e o retorna
        :return: retorna o nome da imagem
        """
        name = self.img_path.split('/')[-1]
        name = name.split('.')
        return name[0]

    def hide_text_dialog(self):
        """
        Abre uma caixa de dialogo que pega do usuario a mensagem que ele quer esconder na imagem
        """
        text, ok = QInputDialog.getText(self, 'Hide Text', 'Message:')
        if ok and text:
            hide_message.apply_transformation(self, self.pixels, text)

    def gamma_correction(self, value):
        """
        Faz os devidos calculos com o valor obtido do slider o convertendo para decimal, e então chama o arquivo que faz
        a correção gamma
        """
        value = (value / 10) / 10
        self.gamma_spin.setValue(value)
        pixel = self.transform_bkup.copy() if self.has_filter else self.pixels_bkup.copy()
        gamma.correction(self, pixel, value)

    def change_tansparency(self, value):
        """
        Pega o valor do slider e transforma em um inteiro corresponde a porcentagem escolhida, chama o arquivo que faz a
        transformação
        """
        percent = int(255 - ((255 * value) / 100))
        print(percent)
        self.transparency_spin.setValue(value)
        transparency.apply_filter(self, self.pixels, percent)

    def set_image(self, pixels, size=None, has_filter=False):
        """
        Atualiza a imagem e o label que mostra a imagem toda vez que ela for modificada
        :param has_filter: serve unicamente para a aplicação de correção gamma
        :param size: tamanho da imagem modificada
        :param pixels: é a imagem modificada recebida de alguma classe que aplica alguma transformação
        """
        self.pixels = pixels.copy()
        if has_filter:
            self.has_filter = has_filter
            self.transform_bkup = pixels.copy()
        if size is not None:
            self.image = self.image.resize(size)
        self.image.putdata(self.pixels)
        self.verify_rotate_or_square()
        self.save_status.setText('   Save Status: Not Saved*   ')
        if self.btn_reset.isEnabled():
            pass
        else:
            self.btn_reset.setEnabled(True)

    def reset(self):
        """
        Reseta a imagem para o status original e desativa o botão de reset que so sera ativado quando a imagem for
        modificada
        """
        self.pixels = self.pixels_bkup.copy()
        self.transform_bkup = self.pixels_bkup.copy()
        size = self.image.size
        if size[1] > size[0]:
            self.image = self.image.resize((size[1], size[0]))
        self.image.putdata(self.pixels_bkup)
        self.verify_rotate_or_square()
        self.has_filter = False
        self.gamma_slider.setValue(100)
        self.gamma_spin.setValue(1)
        self.transparency_slider.setValue(0)
        self.transparency_spin.setValue(0)
        self.btn_reset.setDisabled(True)

    def verify_rotate_or_square(self):
        """
        Verifica se a imagem é quadrada ou se esta rotacionada em 90 ou 270 graus e entaõ define o label de acordo
        """
        size = self.image.size
        q_image = ImageQt(self.image)
        if size[1] > size[0]:
            self.image_label.setPixmap(QPixmap.fromImage(q_image).scaled(400, 400, Qt.KeepAspectRatio))
        else:
            self.image_label.setPixmap(QPixmap.fromImage(q_image).scaled(720, 720, Qt.KeepAspectRatio))


def about_app_dialog():
    """
    Inicia o dialogo que contem as informações do app
    """
    app_dialog = AboutAppDialog()
    app_dialog.exec_()


def secret_message_dialog(message):
    """
    Inicia o dialogo que ira mostrar a mensagem que estava encondida na imagem
    """
    secret_dialog = SecretDialog(message)
    secret_dialog.exec_()


def start():
    """
        Inicia a aplicação
    """
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
