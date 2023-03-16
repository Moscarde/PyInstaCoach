import json
import pyautogui
import pynput

config = {}

# def pega_pos():
#     global pos_url, pos_follow, pos_final_cabecalho, campo_atual
#     pos = pyautogui.position()
#     print(f"Posição {campo_atual} detectada: ", pos )
#     print("....")
#     return pos


# def keydown(tecla):
#     global config, campo_atual
#     if tecla == pynput.keyboard.Key.esc:
#         return False
#     elif tecla == pynput.keyboard.KeyCode(char = "1"):
#         posicao = pega_pos()
#         if posicao:
#             if campo_atual == "url":
#                 config["pos_url"] = posicao
#                 campo_atual = "follow"
#                 return False
#             elif campo_atual == "botao de seguir":
#                 config["pos_follow"] = posicao
#                 pyautogui.screenshot("follow.png", region=(posicao[0]-30, posicao[1]-30, 60, 60))
#                 campo_atual = "pos_final_cabecalho"
#                 return False
#             elif campo_atual == "final da bio":
#                 config["pos_final_cabecalho"] = posicao
#                 return False
#     return True

# def solicita(campo):
#     global campo_atual
#     campo_atual = campo
#     print(f"Coloque o mouse sobre o campo de {campo} e pressione a tecla 1")
#     listener = pynput.keyboard.Listener(on_press=keydown)
#     listener.start()
#     listener.join()

def configura_parametros():
    global config
    print("Iniciando configuração de parametros...")
    config["minimo de follows por dia"] = input("Digite a quantidade minima de Follows diários e pressione ENTER.\n ")
    config["maximo de follows por dia"] = input("Digite a quantidade maxima de Follows diários e pressione ENTER.\n ")
    config["tempo minimo entre follows"] = input("Digite a quantidade minima de pausa entre os follows e pressione ENTER.\n ")
    config["tempo maximo entre follows"] = input("Digite a quantidade maxima de pausa entre os follows e pressione ENTER.\n ")
    print("Configuração concluída!")
    with open("parametros.json", "w") as f:
        json.dump(config, f, indent = 4)

configura_parametros()
