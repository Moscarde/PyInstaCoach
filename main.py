from modules.configura_parametros import configura_parametros
from modules.analisa_contas import analisa_contas
from modules.segue_contas import segue_contas
from modules.configura_coordenadas import *
from modules._ import _
from modules.print_color import *

def exibir_menu():
    print_menu("Escolha uma das opções abaixo e pressione ENTER.")

    print_menu(" [1] Analisar e salvar contas")
    print_menu(" [2] Seguir contas salvas")
    print_menu(" [3] Configurar quantidade de follows diarias e intervalos")
    print_menu(" [4] Fechar script")


def obter_opcao_desejada():
    opcao = input("> ")
    return opcao.strip()


def main():
    exibir_menu()
    opcao = obter_opcao_desejada()

    if opcao == "1":
        analisa_contas()
        main()
    elif opcao == "2":
        segue_contas()
        main()
    elif opcao == "3":
        configura_parametros()
        main()
    elif opcao == "4":
        print("Fechando script...")
        exit()
    elif opcao == "5":
        _()
    else:
        print("Opção inválida. Tente novamente.")
    main()

main()