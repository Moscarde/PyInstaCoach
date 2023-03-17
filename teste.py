import pygetwindow as gw
import time
import pyautogui

def pega_pos():
    global pos_url, pos_follow, pos_final_cabecalho, campo_atual
    pos = pyautogui.position()
    print(f"Posição detectada: ", pos )
    print("....")
    return pos

def printa_pos():
    posicao = pega_pos()
    pyautogui.screenshot("pub.png", region=(posicao[0]-40, posicao[1]-30, 80, 60))


time.sleep(3)

def acha():
    pyautogui.click('publicacoes_btn.png')

# printa_pos()
acha()