"""
Importa a biblioteca PIL usada para a manipulação da imagem
"""
import main_window


def find_message(pixels):
    """
    Encontra o valor escondido no pixel seguindo a logica de que se o valor for menor ou igual do que 27
    ele é um dos numeros que representam uma letra, então esse numero é passado para a função convert_message
    para ser convertido de volta a letra
    """
    message = ''
    for pixel in pixels:
        if pixel[3] <= 15:
            message += convert_message(pixel[3])
    main_window.secret_message_dialog(message)


def convert_message(number):
    """
    Converte um numero recebido no hexa equivalente
    :param number: numero a ser convertido em uma letra
    :return: retorna o valor correspondente em hexa ao numero recebido
    """
    return format(number, 'x')
