import json
import time
import random
import pyautogui
import os
from datetime import datetime
import tkinter as tk
import clipboard
from pynput import keyboard
from modules.manipulacoes_json import *
from modules.configura_parametros import configura_parametros
from modules.configura_coordenadas import configura_coordenadas
from modules.print_color import *


follow_button = "resources/img/follow_btn.png"

min_follow = max_follow = min_espera = max_espera = pos_url = pos_foto_perfil = pos_final_cabecalho = region_cabeçalho = 0
dia_atual = datetime.now().strftime("%d-%m-%Y")
publicacoes_btn = "publicacoes_btn.png"
caminho_coordenadas_segue = "resources/configurations/coordenadas_segue.json"
caminho_parametros = "resources/configurations/parametros.json"
caminho_parametros_padrao = "resources/configurations/parametros_padrao.json"
caminho_lista_de_contas = "resources/lista_de_contas.json"

# Checa se existe o arquivo parametros.json, parametros.json e follow_btn.png
# Carrega dados desses arquivos

def checa_configs():
    if json_checa(caminho_coordenadas_segue):
        global min_follow, max_follow, min_espera, max_espera, pos_url, pos_foto_perfil, pos_final_cabecalho, region_cabeçalho, caminho_coordenadas_seguir, stories
        coordenadas = json_carrega(caminho_coordenadas_segue)
        pos_url = coordenadas["URL"]
        pos_final_cabecalho = coordenadas["Final da bio"]
        pos_foto_perfil = coordenadas["Foto de perfil"]
        largura_tela = pyautogui.size()[1]
        region_cabeçalho = [0, 0, largura_tela, pos_final_cabecalho[1]]

        print("Coordenadas carregadas")
        print("Posição da URL:", pos_url)
        print("Posição final do cabecalho:", pos_final_cabecalho)
        print("Posição foto de perfil:", pos_foto_perfil)
    else:
        print("Coordenadas para o modulo segue contas ainda nao configuradas.")
        print_menu("Deseja iniciar configuracao?")
        print_menu("Digite [1] para SIM e [2] para voltar ao menu:")
        opcao = input(">")

        if opcao == "1":
            configura_coordenadas("segue")
            checa_configs()
        elif opcao == "2":
            return
        else:
            print_erro("Valor Invalido. Repetindo checagem de coordenadas!")
            checa_configs()

    if json_checa(caminho_parametros):
        parametros = json_carrega(caminho_parametros)
        min_follow = parametros["minimo de follows por dia"]
        max_follow = parametros["maximo de follows por dia"]
        min_espera = parametros["tempo minimo entre follows"]
        max_espera = parametros["tempo maximo entre follows"]
        stories = parametros["stories"]
    else:
        print_erro("Parametros ainda não definidos!")
        print_menu("Escolha uma opcao para seguir:")
        print_menu(" [1] Configurar parametros")
        print_menu(" [2] Carregar parametros padroes")
        print_menu(" [3] Voltar para o menu")
        opcao = input(">")

        if opcao == "1":
            configura_parametros()
        elif opcao == "2":
            parametros = json_carrega(caminho_parametros_padrao)
            min_follow = parametros["minimo de follows por dia"]
            max_follow = parametros["maximo de follows por dia"]
            min_espera = parametros["tempo minimo entre follows"]
            max_espera = parametros["tempo maximo entre follows"]
            stories = parametros["stories"]
        elif opcao == "3":
            return
        else:
            print_erro("Valor Invalido. Repetindo checagens.")
            checa_configs()





# def curte_publicacao():
#     pos_publicacoes_btn = pyautogui.locateOnScreen(publicacoes_btn)
#     if pos_publicacoes_btn == None:
#             print("img de publicações nao encontrada")
#             return
#     else:
#         pyautogui.click(pos_publicacoes_btn[0]-50, pos_publicacoes_btn[1]+70)
#         time.sleep(2)
#         pos_like = pyautogui.locateOnScreen(like_button)
#         if pos_like == None:
#             print("img de like nao encontrada")
#         else:
#             pyautogui.click(like_button)
#             time.sleep(1)
#             pyautogui.hotkey("esc")


def visualisa_stories():
    pyautogui.click(pos_foto_perfil)
    time.sleep(2)
    pyautogui.hotkey("right")

def follow(url):
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(url)
    pyautogui.press("enter") 
    time.sleep(4)


    pos_follow = pyautogui.locateOnScreen(follow_button, confidence=0.8, region= region_cabeçalho)
    if pos_follow == None:
        print_nao_seguiu("Botao de seguir nao encontrada, pulando perfil")
        return False
    else:
        print_seguiu("Botao de seguir encontrado")
        pyautogui.click(pos_follow)

        #time.sleep(1.5)
        #curte_publicacao()
        #time.sleep(2)
        if stories:
            visualisa_stories()
        



def aguarde(min, max):
    tempo = random.randint(min, max)
    print("Aguardando " + str(tempo) + " segundos para ir para o proximo perfil")
    time.sleep(tempo)


def tecla_pressionada(key):
    if key == keyboard.Key.esc:
        print("Tecla 'ESC' pressionada. Encerrando...")
        return False

def segue_contas():
    print_menu("Escolha uma das opções abaixo e pressione ENTER:")
    print_menu(" [1] Iniciar modulo de seguir contas")
    print_menu(" [2] Configurar coordenadas")
    print_menu(" [3] Voltar para o menu")
    opcao = input(" >")
    if opcao == "1":
        print_erro("Iniciando modulo. Pressione ESC para parar o script")
    elif opcao == "2":
        configura_coordenadas("segue")
        configura_parametros()
        return segue_contas()
    elif opcao == "3":
        return 
    else:
        return segue_contas()


    global lista_de_contas
    checa_configs()


    # Carrega o arquivo JSON
    if not json_checa(caminho_lista_de_contas):
        print_erro("Nao existe nenhuma lista de contas criadas. Analise e salve algumas contas e tente novamente.")
        return
    
    lista_de_contas = json_carrega(caminho_lista_de_contas)

    qnt_follow = random.randint(min_follow, max_follow)
    print("Quantidade de contas a seguir: ", qnt_follow)


    with keyboard.Listener(on_press=tecla_pressionada) as listener:
        while True:
            # Itera sobre cada objeto no array
            for obj in lista_de_contas:
                # Verifica se a chave "status" tem o valor "Nao seguiu"
                if obj.get("Status") == "Nao seguido":
                    #print("...Segure a tecla ESC para parar o script...")
                    # Imprime a chave "url" do objeto
                    if follow(obj.get("URL")) != False:
                        usuario = obj.get("Nome de usuario")
                        # Atualiza o valor da chave "status" para "Ja seguiu"
                        print_seguiu(f"Seguindo {usuario}")
                        obj["Status"] = "Seguiu"
                        obj["Dia do Follow"] = dia_atual
                        qnt_follow-=1

                        if qnt_follow <= 0:
                            break
                        else:
                            print(f"Restam {qnt_follow} contas para seguir")
                            aguarde(min_espera, max_espera)
                            if not listener.running:
                                break
                    else:
                        obj["Dia do Follow"] = dia_atual
                        obj["Status"] = "Erro"

            if not listener.running:
                break
            break



    # Salva as alterações no arquivo JSON
    json_grava(caminho_lista_de_contas, lista_de_contas)
    

