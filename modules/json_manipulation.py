import json
import os


# Checa se o arquivo foi encontrado
def json_check(caminho):
    if os.path.isfile(caminho):
        return True
    else:
        return False


# Grava o objeto ou array no arquivo
def json_write(caminho, obj):
    with open(caminho, "w") as f:
        json.dump(obj, f, indent = 4)

def json_read(caminho):
    try:
        with open(caminho, "r") as arquivo:
            json_conteudo = json.load(arquivo)
            return json_conteudo
    except FileNotFoundError:
        return False