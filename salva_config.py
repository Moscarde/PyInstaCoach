import pyautogui
# import clipboard
import json
from datetime import datetime
from pynput import keyboard

pos_url = []
pos_follow = []
pos_final_cabecalho = []

def captura_pos(tipo):
    def pega_pos():
        if tipo == 'url':
            x, y = pyautogui.position()
            print(tipo, x, y)
            global pos_url 
            pos_url = [x, y]

        
        if tipo == 'follow':
            x, y = pyautogui.position()
            region_follow = (x-30, y-30, 60, 60)
            print(tipo, x, y)
            global pos_follow
            pos_follow = [x, y]
            pyautogui.screenshot('follow_area.png', region_follow)
        
        if tipo == 'final_cabecalho':
            x, y = pyautogui.position()
            print(tipo, x, y)
            global pos_final_cabecalho
            pos_final_cabecalho = [x, y]

    def tecla_pressionada(key):
        if key == keyboard.KeyCode.from_char('1'):
            pega_pos()
            listener.stop()
    # Cria o objeto listener para o teclado
    listener = keyboard.Listener(on_press=tecla_pressionada)

    # Inicia o listener
    listener.start()

    # Mantém o programa em execução
    listener.join()

def salva_config():
    configs = {'pos_url': pos_url, 'pos_follow': pos_follow, 'pos_final_cabecalho': pos_final_cabecalho}
    with open('config.json', 'w') as f:
        # Escreve a lista de histórico atualizada no arquivo, no formato desejado
        json.dump(configs, f, indent = 4)
    
    print('Salvo!')

print('Iniciando configuração!')
print('Coloque o mouse sobre o campo de url e pressione a tecla 1')
captura_pos('url')
print('Coloque o mouse sobre o centro do botao de seguir e pressione 1')
captura_pos('follow')
print('Coloque o mouse sobre o final do cabecalho e pressione 1')
captura_pos('final_cabecalho')
salva_config()