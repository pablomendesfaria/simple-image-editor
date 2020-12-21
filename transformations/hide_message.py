"""
Importa a classe hashlib
"""
import hashlib


def apply_transformation(parent, pixels, message):
    """
    Esconde a mensagem recebida nos pixels alpha da imagem, primeiro converte cada caractere da mensagem em um numero
    equivalente, e depois coloca esses numeros nos pixels alpha da imagem enquanto a posição do pixel for menor do que
    o tamanho da mensagem, assim colocando a mensagem sempre nos primeiros pixels
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    :param message: mensagem a ser escondida nos pixels alpha da imagem
    """
    sha_256 = hashlib.sha256(message.encode()).hexdigest()
    sha_256_converted = convert_message(sha_256)
    for index, pixel in enumerate(pixels):
        if index < len(sha_256_converted):
            pixels[index] = (pixel[0], pixel[1], pixel[2], sha_256_converted[index])
        else:
            pixels[index] = (pixel[0], pixel[1], pixel[2], pixel[3])
    parent.set_image(pixels)


def convert_message(message):
    """
    Convert a mensagem sha256 em decimal
    :param message: mensagem a ser convertida
    :return: retorna uma lista com os numeros correspondes a cada caractere da mensagem
    """
    message_converted = []
    for char in message:
        message_converted.append(int(f'0x{char}', 16))
    return message_converted
