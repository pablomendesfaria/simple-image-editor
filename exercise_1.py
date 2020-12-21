import subprocess
import sys
from functools import partial
from PyQt5.QtCore import (Qt, QDir)
from PyQt5.QtGui import (QPixmap, QIcon)
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QInputDialog, QWidget, QGridLayout, QLabel, QFileDialog,
                             QApplication)
import transformations


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.menu_bar = self.menuBar()
        self.menu_file = self.menu_bar.addMenu("&File")
        self.action_open_file = self.menu_file.addAction("&Open...")
        self.action_save_file = self.menu_file.addAction("Save As...")
        self.menu_file.addSeparator()
        self.action_exit = self.menu_file.addAction("E&xit")
        self.menu_transformations = self.menu_bar.addMenu("&Transformations")
        self.sub_menu_flip = self.menu_transformations.addMenu("Flip")
        self.action_horizontally = self.sub_menu_flip.addAction("Horizontally")
        self.action_vertically = self.sub_menu_flip.addAction("Vertically")
        self.sub_menu_rotate = self.menu_transformations.addMenu("Rotate")
        self.menu_transformations.addSeparator()
        self.action_90_degrees = self.sub_menu_rotate.addAction("90° Left")
        self.action_180_degrees = self.sub_menu_rotate.addAction("180° Left")
        self.action_270_degrees = self.sub_menu_rotate.addAction("270° Left")
        self.action_gray_scale = self.menu_transformations.addAction("Gray Scale")
        self.menu_transformations.addSeparator()
        self.action_negative = self.menu_transformations.addAction("Negative")
        self.menu_transformations.addSeparator()
        self.action_blur = self.menu_transformations.addAction("Blur")
        self.action_sharpen = self.menu_transformations.addAction("Sharpen")
        self.action_smooth = self.menu_transformations.addAction("Smooth")
        self.menu_transformations.addSeparator()
        self.action_find_edges = self.menu_transformations.addAction("Find Edges")
        self.menu_transformations.addSeparator()
        self.action_shades_of_red = self.menu_transformations.addAction("Shades of Red")
        self.action_shades_of_green = self.menu_transformations.addAction("Shades of Green")
        self.action_shades_of_blue = self.menu_transformations.addAction("Shades of Blue")
        self.menu_transformations.addSeparator()
        self.action_transparency = self.menu_transformations.addAction("Transparency")
        self.menu_steganography = self.menu_bar.addMenu("&Steganography")
        self.action_hide_text = self.menu_steganography.addAction("Hide Text")
        self.action_identify_text = self.menu_steganography.addAction("Identify Secret Text")
        self.menu_help = self.menu_bar.addMenu("&Help")
        self.action_about = self.menu_help.addAction("&About")
        self.about_message = QMessageBox()
        self.widget = QWidget(self)
        self.layout = QGridLayout()
        self.input_image = QLabel(self)
        self.output_image = QLabel(self)
        self.input_path = None
        self.secret_message = QMessageBox()
        self.setup_main_window()
        self.init_ui()

    def setup_main_window(self):
        self.setFixedSize(990, 475)
        self.setWindowTitle("Filter Applicator")
        self.setWindowIcon(QIcon('resources/window_icon.png'))
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.layout)
        self.input_image.setPixmap(QPixmap('resources/image_icon.png').scaled(355, 355, Qt.KeepAspectRatio))
        self.input_image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.input_image, 0, 0)

    def init_ui(self):
        self.action_open_file.triggered.connect(self.open_file)
        self.action_open_file.setShortcut("Alt+O")
        self.action_save_file.triggered.connect(self.save_file)
        self.action_save_file.setShortcut("Ctrl+S")
        self.action_exit.triggered.connect(sys.exit)
        self.action_exit.setShortcut("Alt+X")
        self.action_hide_text.triggered.connect(self.hide_text_dialog)
        self.action_identify_text.triggered.connect(self.identify_message)
        self.action_about.triggered.connect(self.show_about)
        self.action_about.setShortcut("Alt+A")
        self.action_horizontally.triggered.connect(partial(self.apply_transformation, './flip_horizontally.py',
                                                           'flipped_h_image.png'))
        self.action_vertically.triggered.connect(partial(self.apply_transformation, './flip_vertically.py',
                                                         'flipped_y_image.png'))
        self.action_90_degrees.triggered.connect(partial(self.apply_transformation, './rotate_90.py',
                                                         'rotate_90_image.png'))
        self.action_180_degrees.triggered.connect(partial(self.apply_transformation, './rotate_180.py',
                                                          'rotate_180_image.png'))
        self.action_270_degrees.triggered.connect(partial(self.apply_transformation, './rotate_270.py',
                                                          'rotate_270_image.png'))
        self.action_gray_scale.triggered.connect(partial(self.apply_transformation, './gray_scale.py',
                                                         'gray_scale_image.png'))
        self.action_negative.triggered.connect(partial(self.apply_transformation, './negative.py',
                                                       'negative_image.png'))
        self.action_blur.triggered.connect(partial(self.apply_transformation, './blur.py', 'blur_image.png'))
        self.action_sharpen.triggered.connect(partial(self.apply_transformation, './sharpen.py',
                                                      'sharpen_image.png'))
        self.action_smooth.triggered.connect(partial(self.apply_transformation, './smooth_more.py',
                                                     'smooth_image.png'))
        self.action_find_edges.triggered.connect(partial(self.apply_transformation, './find_edge.py',
                                                         'find_edge_image.png'))
        self.action_shades_of_red.triggered.connect(partial(self.apply_transformation, './shades_of_red.py',
                                                            'shades_of_red_image.png'))
        self.action_shades_of_green.triggered.connect(partial(self.apply_transformation, './shades_of_green.py',
                                                              'shades_of_green_image.png'))
        self.action_shades_of_blue.triggered.connect(partial(self.apply_transformation, './shades_of_blue.py',
                                                             'shades_of_blue_image.png'))
        self.action_transparency.triggered.connect(self.transparency_dialog)

    def hide_text_dialog(self):
        text, ok = QInputDialog.getText(self, 'Hide Text', 'Message:')
        if ok and text:
            self.apply_transformation('./hide_message.py', 'hide_message_image.png', message=text)

    def identify_message(self):
        transformations.identify_message.Secret(self, self.input_path)

    def show_secret_message(self, message):
        self.secret_message.setStyleSheet('')
        self.secret_message.setWindowTitle('Secret')
        self.secret_message.setText(f'Secret Message: {message}')
        self.secret_message.exec_()

    def show_about(self):
        self.about_message.setWindowTitle('About')
        self.about_message.setWindowIcon(QIcon('resources/info_icon.png'))
        self.about_message.setIconPixmap(QPixmap('resources/iftm_logo.png').scaled(200, 200, Qt.KeepAspectRatio))
        self.about_message.setText('Desenvolvido por Pablo Mendes Faria')
        self.about_message.setInformativeText('Ituiutaba, 21/11/2020')
        self.about_message.setDetailedText('Programa simples onde se pode abrir uma imagem e aplicar ums dos filtros '
                                           'disponiveis (Gray Scale, Negative, Blur, Sharpen, Smooth, Find Edges, '
                                           'Shades of Red, Shades of Green e Shades of Blue).')
        self.about_message.exec_()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), 'All Files (*.*);;'
                                                                                          'Images (*.png; *.jpg)',
                                                   'Images (*.png; *.jpg)')
        self.input_path = file_name
        self.input_image.setPixmap(QPixmap(self.input_path).scaled(455, 455, Qt.KeepAspectRatio))

    def save_file(self):
        if True:
            None

    def transparency_dialog(self):
        percentage, ok = QInputDialog.getInt(self, 'Transparency', 'Percentage:', 0, 0, 100, 1)
        if ok and percentage != 0:
            self.apply_transformation('./transparency.py', f'transparency_{percentage}%_image.png', percentage)

    def apply_transformation(self, algorithm, output_path, transparency=0, gamma=0, message=''):
        command = f'python {algorithm} "{self.input_path}" {output_path} {int((255 * transparency) / 100)} {gamma} ' \
                  f'"{message.lower()}"'
        subprocess.run(command, True)
        self.output_image.setPixmap(QPixmap(output_path).scaled(455, 455, Qt.KeepAspectRatio))


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
