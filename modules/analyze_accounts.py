import pyautogui
import clipboard
from datetime import datetime
from pynput import keyboard
from modules.json_manipulation import *
from modules.configure_coordinates import *
from modules.check_accounts import check_accounts
from modules.print_color import *




pos_url = []
path_accounts_list = "resources/accounts_list.json"
path_analyse_coordinates = "resources/configurations/analyze_coordinates.json"




# Verify if coordinates exist
def check_coordinates():
    if json_check(path_analyse_coordinates):
        global pos_url
        coordinates = json_read(path_analyse_coordinates)
        pos_url = coordinates["URL"]
        print("Coordenadas carregadas")
        print("Posição da URL:", pos_url)
    else:
        print_red("Coordenadas para o modulo analise de contas ainda nao configuradas.")
        print_cyan("Deseja iniciar configuracao?")
        print_cyan("Digite [1] para SIM e [2] para NAO:")
        opcao = input(">")

        if opcao == "1":
            configure_coordinates("analyze")
            check_coordinates()
        elif opcao == "2":
            return
        else:
            print_red("Valor Invalido. Repetindo checagem de coordenadas!")
            check_coordinates()

def save_url():
    global pos_url

    # Move to URL coordinates
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "w")

    # Get clipboard URL
    url = clipboard.paste()

    # Get user name 
    user = url.split("/")[-2]
    print_green(f"@{user}")

    # Get current day
    current_day = datetime.now().strftime("%d-%m-%Y")

    # Create new account object
    new_account = {"URL": url, "User": user, "Save account day": current_day, "Status": "Not followed"}

    # Verify if accounts list alread exists and append new account
    if json_check(path_accounts_list):
        accounts_list = json_read(path_accounts_list)
    else:
        accounts_list = []

    accounts_list.append(new_account)
    json_write(path_accounts_list, accounts_list)

# Move to URL and close tab
def close_tab():
    global pos_url
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "w")

# Show options
def show_options():
    print_cyan("Pressione a tecla correspondente:\n [1] Salvar a url da conta\n [2] Pular conta e fechar guia\n [3] Configurar coordenadas\n [4] Sair para o menu")

# Verify pressed key and calls the respective function
def on_press(key):
    if not hasattr(key, 'vk'):
        return
    
    if key == keyboard.KeyCode.from_char("1") or key.vk == 97:
        print_green("Salvando url...")
        save_url()
        show_options()

    if key == keyboard.KeyCode.from_char("2") or key.vk == 98:
        print_pink("Fechando aba...")
        close_tab()
        show_options()

    if key == keyboard.KeyCode.from_char("3") or key.vk == 99:
        print("Configurando coordenadas...")
        configure_coordinates("analyze")
        return False

    if key == keyboard.KeyCode.from_char("4") or key.vk == 100:
        print("Voltando para o menu...")
        return False

# Main function
def analyze_accounts():
    print("Iniciando modulo analise de contas...")

    # Check if account list exists
    check_accounts()
    # Check if coordinates settings exists
    check_coordinates()

    print("Checagens concluidas...")

    # Print instructions / options
    show_options()

    # Keyboard keypress listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()