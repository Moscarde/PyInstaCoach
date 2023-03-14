import pyautogui
import clipboard
import json
from datetime import datetime
from pynput import keyboard

print('Pressione 1 para capturar url e 2 para pular usuario e 3 para sair')

def copia():
    pyautogui.click(x=300, y=60) 
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'w')
def salva():
    # Obtém o conteúdo atual do clipboard (url)
    url = clipboard.paste()
    usuario = url.split("/")[-2]

    # Obtém a hora atual
    dia_atual = datetime.now().strftime('%d-%m-%Y')

    # Cria um novo objeto com as informações do clipboard e da hora atual
    new_clipboard_item = {'url': url, 'Nome de usuario': usuario, 'dia': dia_atual, 'status': 'Nao seguiu', 'SDV': 'Nao'}

    try:
        # Tenta abrir o arquivo JSON em modo de leitura
        with open('clipboard_history.json', 'r') as f:
            # Tenta carregar o conteúdo do arquivo JSON
            clipboard_history = json.load(f)
    except FileNotFoundError:
        # Se o arquivo não existir, inicializa a lista com o novo objeto
        clipboard_history = [new_clipboard_item]
    else:
        # Se o arquivo existir, adiciona o novo objeto na lista de histórico do clipboard
        clipboard_history.append(new_clipboard_item)

    # Abre o arquivo JSON em modo de gravação
    with open('clipboard_history.json', 'w') as f:
        # Escreve a lista de histórico atualizada no arquivo, no formato desejado
        json.dump(clipboard_history, f, indent = 4)
    
    print('Salvo!')
def fecha():
    pyautogui.click(x=300, y=60) 
    pyautogui.hotkey('ctrl', 'w')

def tecla_pressionada(key):
    if key == keyboard.KeyCode.from_char('1'):
        print('Tentando coletar url')
        copia()
        salva()
        print('Coletada com sucesso!')

    if key == keyboard.KeyCode.from_char('2'):
        print('Fechando aba')
        fecha()

    if key == keyboard.KeyCode.from_char('3'):
        print('Interrompendo script')
        exit()



# Cria o objeto listener para o teclado
listener = keyboard.Listener(on_press=tecla_pressionada)

# Inicia o listener
listener.start()

# Mantém o programa em execução
listener.join()
