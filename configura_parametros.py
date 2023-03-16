import json
import pyautogui
import pynput

config = {}


def configura_parametros():
    global config
    print("Iniciando configuração de parametros...")
    config["minimo de follows por dia"] = int(input("Digite a quantidade minima de Follows diários e pressione ENTER.\n "))
    config["maximo de follows por dia"] = int(input("Digite a quantidade maxima de Follows diários e pressione ENTER.\n "))
    config["tempo minimo entre follows"] = int(input("Digite a quantidade minima de pausa entre os follows e pressione ENTER.\n "))
    config["tempo maximo entre follows"] = int(input("Digite a quantidade maxima de pausa entre os follows e pressione ENTER.\n "))
    print("Configuração concluída!")
    with open("parametros.json", "w") as f:
        json.dump(config, f, indent = 4)


