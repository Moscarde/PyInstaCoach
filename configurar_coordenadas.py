import json
import pyautogui
import pynput

config = {}

def pega_pos():
    global pos_url, pos_follow, pos_final_cabecalho, campo_atual
    pos = pyautogui.position()
    print(f"Posição {campo_atual} detectada: ", pos )
    print("....")
    return pos


def keydown(tecla):
    global config, campo_atual
    if tecla == pynput.keyboard.Key.esc:
        return False
    elif tecla == pynput.keyboard.KeyCode(char = '1'):
        posicao = pega_pos()
        if posicao:
            if campo_atual == "url":
                config["pos_url"] = posicao
                campo_atual = "follow"
                return False
            elif campo_atual == "follow":
                config["pos_follow"] = posicao
                campo_atual = "cabecalho"
                return False
            else:
                config["pos_final_cabecalho"] = posicao
                return False
    return True

def solicita(campo):
    global campo_atual
    campo_atual = campo
    print(f"Coloque o mouse sobre o campo de {campo} e pressione a tecla 1")
    listener = pynput.keyboard.Listener(on_press=keydown)
    listener.start()
    listener.join()

def configurar_coordenadas():
    global config
    print("Iniciando configuração...")
    solicita('url')
    solicita('follow')
    solicita('cabecalho')
    print("Configuração concluída!")
    with open('config.json', 'w') as f:
        json.dump(config, f)

configurar_coordenadas()
