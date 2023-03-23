import time
import random
import pyautogui
from datetime import datetime
from pynput import keyboard
from modules.json_manipulation import *
from modules.configure_parameters import configure_parameters
from modules.configure_coordinates import configure_coordinates
from modules.check_accounts import check_accounts
from modules.print_color import *
from tqdm import tqdm


follow_button = "resources/img/follow_btn.png"

min_follow = max_follow = min_wait = max_wait = pos_url = pos_profile_picture = pos_head_end = head_region = 0
current_day = datetime.now().strftime("%d-%m-%Y")
path_parameters = "resources/configurations/parameters.json"
path_default_parameters = "resources/configurations/default_parameters.json"
path_follow_coordinates = "resources/configurations/follow_coordinates.json"
path_accounts_list = "resources/accounts_list.json"

# Verify if coordinates exist
def check_config():
    if json_check(path_follow_coordinates):
        global min_follow, max_follow, min_wait, max_wait, pos_url, pos_profile_picture, pos_head_end, head_region, caminho_coordenadas_seguir, stories
        coordenadas = json_read(path_follow_coordinates)
        pos_url = coordenadas["URL"]
        pos_profile_picture = coordenadas["Profile Picture"]
        pos_head_end = coordenadas["Head End"]
        screen_width = pyautogui.size()[1]
        head_region = [0, 0, screen_width, pos_head_end[1]]

        print("Coordenadas carregadas")
        print("Posição da URL:", pos_url)
        print("Posição final do cabecalho:", pos_head_end)
        print("Posição foto de perfil:", pos_profile_picture)
    else:
        print_red("Coordenadas para o modulo segue contas ainda nao configuradas.")
        print_cyan("Deseja iniciar configuracao?")
        print_cyan("Digite [1] para SIM e [2] para voltar ao menu:")
        option = input(">")

        if option == "1":
            configure_coordinates("follow")
            check_config()
        elif option == "2":
            return
        else:
            print_red("Valor Invalido. Repetindo checagem de coordenadas!")
            check_config()

    if json_check(path_parameters):
        parameters = json_read(path_parameters)
        min_follow = parameters["Minimum follows per day"]
        max_follow = parameters["Maximum follows per day"]
        min_wait = parameters["Minimum time between follows"]
        max_wait = parameters["Maximum time between follows"]
        stories = parameters["Watch stories"]
    else:
        print_red("Parametros ainda não definidos!")
        print_cyan("Digite o numero correspondente a uma opcao e pressione ENTER:")
        print_cyan(" [1] Configurar parametros")
        print_cyan(" [2] Carregar parametros padroes")
        print_cyan(" [3] Voltar para o menu")
        option = input(">")

        if option == "1":
            configure_parameters()
        elif option == "2":
            parameters = json_read(path_default_parameters)
            min_follow = parameters["Minimum follows per day"]
            max_follow = parameters["Maximum follows per day"]
            min_wait = parameters["Minimum time between follows"]
            max_wait = parameters["Maximum time between follows"]
            stories = parameters["Watch stories"]
        elif option == "3":
            return
        else:
            print_red("Valor Invalido. Repetindo checagens.")
            check_config()

# Click in profile picture position
def watch_stories():
    time.sleep(2)
    pyautogui.click(pos_profile_picture)
    time.sleep(2)
    pyautogui.hotkey("right")

# Main function
def follow(url):
    # Click in URL position and paste url
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(url)
    pyautogui.press("enter") 
    time.sleep(4)

    # Try to find follow button image before click it
    pos_follow = pyautogui.locateOnScreen(follow_button, confidence=0.8, region= head_region)
    if pos_follow == None:
        print_red("Botao de seguir nao encontrada, pulando perfil")
        return False
    else:
        print_green("Botao de seguir encontrado")
        pyautogui.click(pos_follow)

        # Verify watch stories status
        if stories:
            watch_stories()

# Wait a while between follows
def wait(min, max):
    wait_time = random.randint(min, max)
    print("Aguardando " + str(wait_time) + " segundos para ir para o proximo perfil")
    for i in tqdm(range(wait_time)):
        time.sleep(1)

# Verify esc key press
def on_press(key):
    if key == keyboard.Key.esc:
        print("Tecla 'ESC' pressionada. Encerrando...")
        return False

# Main function
def follow_accounts():
    global accounts_list

    # Show options
    print_cyan("Escolha uma das opções abaixo e pressione ENTER:")
    print_cyan(" [1] Iniciar modulo de seguir contas")
    print_cyan(" [2] Configurar coordenadas")
    print_cyan(" [3] Voltar para o menu")
    option = input(" >")

    if option == "1":
        print_red("Iniciando modulo")
    elif option == "2":
        configure_coordinates("follow")
        configure_parameters()
        return follow_accounts()
    elif option == "3":
        return 
    else:
        return follow_accounts()

    # Verify configuration
    check_config()

    # Verify if accounts list exists
    if check_accounts() == False:
        return
    
    accounts_list = json_read(path_accounts_list)

    qnt_follow = random.randint(min_follow, max_follow)
    print("Quantidade de contas a seguir: ", qnt_follow)

    print_red("Pressione ESC para parar o script")
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            for obj in accounts_list:
                if obj.get("Status") == "Not followed":
                    # Try find and click follow btn
                    if follow(obj.get("URL")) != False:
                        User = obj.get("User")
                        print_green(f"Seguindo {User}")
                        obj["Status"] = "Followed"
                        obj["Follow date"] = current_day
                        qnt_follow-=1

                        if qnt_follow <= 0:
                            break
                        else:
                            print(f"Restam {qnt_follow} contas para seguir")
                            wait(min_wait, max_wait)
                            if not listener.running:
                                break
                    else:
                        obj["Follow date"] = current_day
                        obj["Status"] = "Follow btn not found"

            if not listener.running:
                break
            break



    # Salva as alterações no arquivo JSON
    json_write(path_accounts_list, accounts_list)
    

