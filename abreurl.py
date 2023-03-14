import json
import time
import random
import pyautogui


follow_button = 'follow.png'

def follow(url):
    pyautogui.click(x=300, y=60) 
    pyautogui.write(url)
    pyautogui.press('enter') 
    time.sleep(4)


    posicao = pyautogui.locateOnScreen(follow_button, confidence=0.8)

        # Verifica se a imagem foi encontrada
    if posicao is not None:
        print(posicao)
        # Obtém a posição central da imagem
        x, y, largura, altura = posicao
        centro_x = x + largura // 2
        centro_y = y + altura // 2

            # Imprime a posição central da imagem
        print(f"A imagem foi encontrada na posição ({centro_x}, {centro_y}).")
        pyautogui.click(centro_x, centro_y) 
    else:
        print("A imagem não foi encontrada.")

    
def aguarde():
    tempo = random.randint(5, 15)
    print('Aguardando ' + str(tempo) + ' Segundos')
    time.sleep(tempo)

# Define o caminho do arquivo JSON
json_path = "clipboard_history.json"




# Carrega o arquivo JSON
with open(json_path) as file:
    data = json.load(file)

# Itera sobre cada objeto no array
for obj in data:
    # Verifica se a chave "status" tem o valor "Nao seguiu"
    if obj.get("status") == "Nao seguiu":
        # Imprime a chave "url" do objeto
        follow(obj.get("url"))
        print(obj.get("url"))
        # Atualiza o valor da chave "status" para "Ja seguiu"
        obj["status"] = "Ja seguiu"
        aguarde()

# Salva as alterações no arquivo JSON
with open(json_path, "w") as file:
    json.dump(data, file)

