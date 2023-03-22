import pyautogui
import clipboard
import json
from datetime import datetime
from pynput import keyboard
from modules.manipulacoes_json import *
from modules.configura_coordenadas import *
import time
from modules.checa_contas import checa_contas
from modules.print_color import *




pos_url = []
pos_final_cabecalho = []
caminho_lista_de_contas = "resources/lista_de_contas.json"
caminho_coordenadas_analise = "resources/configurations/coordenadas_analise.json"




# Checa se existe o arquivo coordenadas_analise.json
def checa_configs():
    if json_checa(caminho_coordenadas_analise):
        global pos_url, pos_primeira_conta
        configuracoes = json_carrega(caminho_coordenadas_analise)
        pos_url = configuracoes["URL"]
        print("Coordenadas carregadas")
        print("Posição da URL:", pos_url)
    else:
        print_erro("Coordenadas para o modulo analise de contas ainda nao configuradas.")
        print_menu("Deseja iniciar configuracao?")
        print_menu("Digite [1] para SIM e [2] para NAO:")
        opcao = input(">")

        if opcao == "1":
            configura_coordenadas("analisa")
            checa_configs()
        elif opcao == "2":
            return
        else:
            print_erro("Valor Invalido. Repetindo checagem de coordenadas!")
            checa_configs()

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
    print_seguiu(f"@{usuario}")

    # Obtem o dia atual
    dia_atual = datetime.now().strftime("%d-%m-%Y")

    # Cria um novo objeto com as informações do clipboard e da hora atual
    nova_conta = {"URL": url, "Nome de usuario": usuario, "Dia": dia_atual, "Status": "Nao seguido", "SDV": "Nao"}

    # Verifica se o arquivo lista_de_contas.json para carregar os dados já existentes
    lista_de_contas = json_carrega(caminho_lista_de_contas)
    lista_de_contas.append(nova_conta)
    json_grava(caminho_lista_de_contas, lista_de_contas)

def fecha_guia():
    pyautogui.click(x=300, y=60) 
    pyautogui.hotkey("ctrl", "w")


def mostra_menu():
    print_menu("Pressione a tecla correspondente:\n [1] Salvar a url da conta\n [2] Pular conta e fechar guia\n [3] Configurar coordenadas\n [4] Sair para o menu")



def tecla_pressionada(key):
    if not hasattr(key, 'vk'):
        return
    
    if key == keyboard.KeyCode.from_char("1") or key.vk == 97:
        print_seguiu("Salvando url...")
        salva_url()
        mostra_menu()

    if key == keyboard.KeyCode.from_char("2") or key.vk == 98:
        print_nao_seguiu("Fechando aba...")
        fecha_guia()
        mostra_menu()

    if key == keyboard.KeyCode.from_char("3") or key.vk == 99:
        print("Configurando coordenadas...")
        configura_coordenadas("analisa")
        return False

    if key == keyboard.KeyCode.from_char("4") or key.vk == 100:
        print("Voltando para o menu...")
        return False

def analisa_contas():
    print("Iniciando modulo analise de contas...")
    print("Checando lista de contas...")
    checa_contas()
    print("Checando coordenadas do modulo...")
    checa_configs()
    print('Checagens concluidas...')

    # Instrucoes para o usuario
    mostra_menu()

    # Cria o objeto listener para o teclado
    listener = keyboard.Listener(on_press=tecla_pressionada)
    listener.start()
    listener.join()