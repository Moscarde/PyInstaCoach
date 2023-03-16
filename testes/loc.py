import pyautogui
from pynput import keyboard

# Define o caminho para a imagem a ser localizada
imagem = 'pip.png'

# Função para lidar com o evento de tecla pressionada
def tecla_pressionada(key):
    if key == keyboard.KeyCode.from_char('1'):
        # Localiza a posição da imagem na tela
        posicao = pyautogui.locateOnScreen(imagem)

        # Verifica se a imagem foi encontrada
        if posicao is not None:
            # Obtém a posição central da imagem
            x, y, largura, altura = posicao
            centro_x = x + largura // 2
            centro_y = y + altura // 2

            # Imprime a posição central da imagem
            print(f"A imagem foi encontrada na posição ({centro_x}, {centro_y}).")
        else:
            print("A imagem não foi encontrada.")

# Cria o objeto listener para o teclado
listener = keyboard.Listener(on_press=tecla_pressionada)

# Inicia o listener
listener.start()

# Mantém o programa em execução
listener.join()
