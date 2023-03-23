from modules.configure_parameters import configure_parameters
from modules.analyze_accounts import analyze_accounts
from modules.follow_accounts import follow_accounts
from modules.configure_coordinates import *
from modules._ import _
from modules.print_color import *

def show_options():
    print_cyan("Escolha uma das opções abaixo e pressione ENTER.")
    print_cyan(" [1] Analisar e salvar contas")
    print_cyan(" [2] Seguir contas salvas")
    print_cyan(" [3] Configurar quantidade de follows diarias e intervalos")
    print_cyan(" [4] Fechar script")

# Main function (Modules options)
def main():
    print_bold("Bem vindo ao PyInstaCoach")
    show_options()
    option = input("> ")

    if option == "1":
        analyze_accounts()
        main()
    elif option == "2":
        follow_accounts()
        main()
    elif option == "3":
        configure_parameters()
        main()
    elif option == "4":
        print("Fechando script...")
        exit()
    elif option == "5":
        _()
    else:
        print("Opção inválida. Tente novamente.")
    main()

main()