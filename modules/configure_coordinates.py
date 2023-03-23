import json
import pyautogui
import pynput
from modules.json_manipulation import *
from modules.print_color import *


config = {}
path_analyze_coordinates = "resources/configurations/analyze_coordinates.json"
path_follow_coordinates = "resources/configurations/follow_coordinates.json"

# Capture position and region screenshot
def get_pos():
    global current_field, screenshot
    pos = pyautogui.position()
    print(f"Posição {current_field} detectada: ", pos )
    if screenshot:
        pyautogui.screenshot(f"resources/img/{screenshot}.png", region=(pos[0]-30, pos[1]-15, 60, 30))
        print(f"Botao capturado e salva em resources/img/{screenshot}.png")
    print("....")
    return pos

# Verify pressed key and calls get_pos()
def on_press(key):
    global pos_current
    if key == pynput.keyboard.Key.esc:
        return False
    elif key == pynput.keyboard.KeyCode(char = "1"):
        pos_current = get_pos()
        return False


def request(field, *args):
    global current_field, pos_current, screenshot
    current_field = field

    if args:
        screenshot = args[0]
    else:
        screenshot = False

    print(f"Coloque o mouse sobre o CENTRO do campo de {field} e pressione a tecla 1")
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    return pos_current

# Main function
# Request cursor positions
def configure_coordinates(module):
    global config
    print("Iniciando configuração...")
    print_red("Para uma referencia visual de onde posicionar o mouse, veja a pasta PICTURES")
    print("Abra uma pagina de um perfil que voce ainda nao seguiu")

    if module == "analyze":
        config["URL"] = request("URL")
        json_write(path_analyze_coordinates, config)
    if module == "follow":
        config["URL"] = request("URL")
        config["Follow Btn"] = request("Botao seguir", "follow_btn")
        config["Profile Picture"] = request("Foto de perfil")
        config["Head End"] = request("Final da bio")
        json_write(path_follow_coordinates, config)
    
    print(f"Configuracoes do modulo {module} finalizada!")


