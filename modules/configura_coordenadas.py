import json
import pyautogui
import pynput
from modules.manipulacoes_json import *
from modules.print_color import *


config = {}
caminho_coordenadas_analise = "resources/configurations/coordenadas_analise.json"
caminho_coordenadas_segue = "resources/configurations/coordenadas_segue.json"
def pega_pos():
    global campo_atual, captura_screenshot
    pos = pyautogui.position()
    print(f"Posição {campo_atual} detectada: ", pos )
    if captura_screenshot:
        pyautogui.screenshot(f"resources/img/{captura_screenshot}.png", region=(pos[0]-30, pos[1]-15, 60, 30))
        print(f"Botao capturado e salva em resources/img/{captura_screenshot}.png")
    print("....")
    return pos


def keydown(tecla):
    global pos_atual
    if tecla == pynput.keyboard.Key.esc:
        return False
    elif tecla == pynput.keyboard.KeyCode(char = "1"):
        pos_atual = pega_pos()
        return False


def solicita(campo, *screenshot):
    global campo_atual, pos_atual, captura_screenshot
    campo_atual = campo
    if screenshot:
        captura_screenshot = screenshot[0]
    else:
        captura_screenshot = False

    print(f"Coloque o mouse sobre o CENTRO do campo de {campo} e pressione a tecla 1")
    listener = pynput.keyboard.Listener(on_press=keydown)
    listener.start()
    listener.join()
    return pos_atual

def configura_coordenadas(modulo):
    global config
    print("Iniciando configuração...")
    print_erro("Para uma referencia visual de onde posicionar o mouse, veja a pasta TUTORIAIS")
    print("Abra uma pagina de um perfil que voce gostaria de seguir seus seguidores")
    if modulo == "analisa":
        config["URL"] = solicita("URL")
        json_grava(caminho_coordenadas_analise, config)
    if modulo == "segue":
        config["URL"] = solicita("URL")
        config["Botao seguir"] = solicita("Botao seguir", "follow_btn")
        config["Foto de perfil"] = solicita("Foto de perfil")
        config["Final da bio"] = solicita("Final da bio")
        json_grava(caminho_coordenadas_segue, config)

    
    print(f"Configuracoes do modulo {modulo} finalizada!")


