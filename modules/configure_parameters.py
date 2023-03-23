import json
import pyautogui
import pynput

config = {}
caminho_parametros = "resources/configurations/parameters.json"

# Request user preferences
def configure_parameters():
    global config
    print("Iniciando configuração de parametros...")
    config["Minimum follows per day"] = int(input("Digite a quantidade minima de Follows diários e pressione ENTER.\n "))
    config["Maximum follows per day"] = int(input("Digite a quantidade maxima de Follows diários e pressione ENTER.\n "))
    config["Minimum time between follows"] = int(input("Digite a quantidade minima de pausa entre os follows e pressione ENTER.\n "))
    config["Maximum time between follows"] = int(input("Digite a quantidade maxima de pausa entre os follows e pressione ENTER.\n "))
    config["Watch stories"] = int(input("Assistir stories caso tenha? [1]Sim [2]Nao.\n "))
    print("Configuração concluída!")
    with open(caminho_parametros, "w") as f:
        json.dump(config, f, indent = 4)


