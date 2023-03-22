from modules.manipulacoes_json import *
from modules.print_color import *

caminho_lista_de_contas = "resources/lista_de_contas.json"

def checa_contas():
    if json_checa(caminho_lista_de_contas):
        lista_de_contas = json_carrega(caminho_lista_de_contas)
        quant = 0
        for objeto in lista_de_contas:
            if objeto["Status"] == "Seguiu":
                quant += 1
        contas_seguidas = quant
        contas_nao_seguidas = len(lista_de_contas) - contas_seguidas
        print('Lista de contas carregada')
        print('Existem', contas_seguidas, 'contas ja seguidas')
        print('Existem', contas_nao_seguidas, 'contas ainda nao seguidas. *Porém podem conter erros*')

    else:
        print_erro('Lista de contas vazia')
        return False