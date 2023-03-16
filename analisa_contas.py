import pyautogui
import clipboard
import json
from datetime import datetime
from pynput import keyboard




pos_url = []
pos_final_cabecalho = []



# Checa se existe o arquivo coordenadas.json e follow_btn.png
def checa_configs():
    try:
        with open("coordenadas.json", "r") as arquivo:
            dados_json = json.load(arquivo)
    except FileNotFoundError:
        print("O arquivo de coordenadas não existe. Configure-o antes e tente novamente.")
        return False
    else:
        global pos_url, pos_final_cabecalho
        pos_url = dados_json["pos_url"]
        pos_final_cabecalho = dados_json["pos_final_cabecalho"]

        print("Posição da URL:", pos_url)
        print("Posição final do cabeçalho:", pos_final_cabecalho)

def salva_url():
    global pos_url

    # Move o cursor até as coordenadas da url
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "w")

    # Obtem o conteudo copiado
    url = clipboard.paste()

    # Salva o nome de usuario
    usuario = url.split("/")[-2]
    print("@", usuario)

    # Obtem o dia atual
    dia_atual = datetime.now().strftime("%d-%m-%Y")

    # Cria um novo objeto com as informações do clipboard e da hora atual
    dados_conta = {"URL": url, "Nome de usuario": usuario, "Dia": dia_atual, "Status": "Nao seguiu", "SDV": "Nao", "Dia do Follow" : "..."}

    # Verifica se o arquivo lista_de_contas.json para carregar os dados já existentes
    try:
        with open("lista_de_contas.json", "r") as f:
            lista_de_contas = json.load(f)
    except FileNotFoundError:
        lista_de_contas = [dados_conta]
    else:
        lista_de_contas.append(dados_conta)

    # Abre o arquivo JSON em modo de gravação
    with open("lista_de_contas.json", "w") as f:
        # Salva o arquivo atualizado com os novos dados
        json.dump(lista_de_contas, f, indent = 4)

def fecha_guia():
    pyautogui.click(x=300, y=60) 
    pyautogui.hotkey("ctrl", "w")




def tecla_pressionada(key):
    if key == keyboard.KeyCode.from_char("1"):
        print("Salvando url...")
        salva_url()

    if key == keyboard.KeyCode.from_char("2"):
        print("Fechando aba...")
        fecha_guia()

    if key == keyboard.KeyCode.from_char("3"):
        print("Interrompendo script...")
        exit()


def analisa_contas():
    # Faz uma checagem de arquivos antes de iniciar o script
    if checa_configs() == False:
        exit()

    # Instrucoes para o usuario
    print("Pressione [1] para salvar a url da conta e [2] para pular a conta e fechar guia e [3] para sair.")
    # Cria o objeto listener para o teclado
    listener = keyboard.Listener(on_press=tecla_pressionada)

    listener.start()
    listener.join()


