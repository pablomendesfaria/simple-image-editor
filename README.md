# Descrição:

Um simples programa de edição de imagem que possui funcionalidade de abrir, salvas como e salvar uma imagem
além de alguns filtros e transformações como escala de cinza, negativo, transparência e correção gama.
O programa também conta com um sistema simples de Esteganografia com SHA256, onde o usuário pode esconder
uma senha de ate 6 caracteres (A-Z0-9@;:<>=?) na imagem, que será criptografada para SHA256 e então adicionada
a camada alpha da imagem nos primeiros N pixels da imagem.
Da mesma forma também conta um sistema para quebrar a senha escondida feito em Java.

# Tecnologias:

Python, biblioteca Pillow e Pyqt5, ambas as bibliocas são necessarias, os comandos para instalar cada uma 
delas segue abaixo.

[pip install Pillow](https://pypi.org/project/Pillow/)

[pip install PyQt5](https://pypi.org/project/PyQt5/)

[pip install pyqt5-tools](https://pypi.org/project/pyqt5-tools/)

# ScreenShots:

![Screenshot_1](https://user-images.githubusercontent.com/48353092/100550732-a3b62200-325a-11eb-9dd1-1eec989869a6.png)

![Screenshot_3](https://user-images.githubusercontent.com/48353092/100550737-b2043e00-325a-11eb-8bb0-a5aa8784ce5d.png)

# Integrantes:

Pablo Mendes Faria.
