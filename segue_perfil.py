import json
import time
import random
import pyautogui
import os
from datetime import datetime
import tkinter as tk


follow_button = "follow_btn.png"
min_follow = max_follow = min_espera = max_espera = pos_url = pos_foto_perfil = pos_final_cabecalho = region_cabeçalho = 0
dia_atual = datetime.now().strftime("%d-%m-%Y")

# Checa se existe o arquivo parametros.json, parametros.json e follow_btn.png
# Carrega dados desses arquivos
def checa_configs():
    global min_follow, max_follow, min_espera, max_espera, pos_url, pos_foto_perfil, pos_final_cabecalho, region_cabeçalho
    try:
        with open("parametros.json", "r") as arquivo:
            parametros_config = json.load(arquivo)
    except FileNotFoundError:
        print("O arquivo de configuração de follow não existe. Configure-o antes e tente novamente.")
        return False
    else:
        min_follow = parametros_config["minimo de follows por dia"]
        max_follow = parametros_config["maximo de follows por dia"]
        min_espera = parametros_config["tempo minimo entre follows"]
        max_espera = parametros_config["tempo maximo entre follows"]

    follow_btn = "follow_btn.png"
    if os.path.isfile(follow_btn) == False:
        print("O arquivo", follow_btn, "não existe no diretório atual. Configure-o antes e tente novamente.")
        return False
    
    try:
        with open("coordenadas.json", "r") as arquivo:
            coordenadas_config = json.load(arquivo)
    except FileNotFoundError:
        print("O arquivo de coordenadas não existe. Configure-o antes e tente novamente.")
        return False
    else:
        pos_url = coordenadas_config["pos_url"]
        pos_final_cabecalho = coordenadas_config["pos_final_cabecalho"]
        pos_foto_perfil = coordenadas_config["pos_foto_perfil"]

        root = tk.Tk()
        largura_tela = root.winfo_screenwidth()
        root.destroy()
        region_cabeçalho = [0, 0, largura_tela, pos_final_cabecalho[1]]

def follow(url):
    pyautogui.click(pos_url) 
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(url)
    pyautogui.press("enter") 
    time.sleep(4)


    pos_follow = pyautogui.locateOnScreen(follow_button, confidence=0.8, region= region_cabeçalho)
    if pos_follow == None:
        print("img de follow nao encontrada, pulando perfil")
        return False
    else:
        print("img encontrada")
        pyautogui.click(pos_follow)
        time.sleep(1)
        pyautogui.click(pos_foto_perfil)
        time.sleep(2)
        pyautogui.hotkey("right")



def aguarde(min, max):
    tempo = random.randint(min, max)
    print("Aguardando " + str(tempo) + " segundos para ir para o proximo perfil")
    time.sleep(tempo)




def segue_perfil():
    if checa_configs() == False:
        exit()
    
    qnt_follow = random.randint(min_follow, max_follow)
    print("Quantidade de contas a seguir: ", qnt_follow)

    # Carrega o arquivo JSON
    with open("lista_de_contas.json") as file:
        lista_de_contas = json.load(file)

    # Itera sobre cada objeto no array
    for obj in lista_de_contas:
        

        # Verifica se a chave "status" tem o valor "Nao seguiu"
        if obj.get("Status") == "Nao seguiu":
            # Imprime a chave "url" do objeto
            if follow(obj.get("URL")) != False:
                # Atualiza o valor da chave "status" para "Ja seguiu"
                print("Seguindo", obj.get("Nome de usuario"))
                obj["Status"] = "Ja seguiu"
                obj["Dia do Follow"] = dia_atual
                qnt_follow-=1

                if qnt_follow <= 0:
                    break
                else:
                    aguarde(min_espera, max_espera)
            else:
                obj["Dia do Follow"] = dia_atual
                obj["Status"] = "Erro"



    # Salva as alterações no arquivo JSON
    with open("lista_de_contas.json", "w") as file:
        json.dump(lista_de_contas, file, indent=4)
    
