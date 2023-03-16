from configura_coordenadas import configura_coordenadas
from configura_parametros import configura_parametros
from analisa_contas import analisa_contas
from segue_perfil import segue_perfil

def exibir_menu():
    print("Bem-vindo ao nosso programa!")
    print("Escolha uma das opções abaixo:")
    print(" [1] Configurar coordenadas")
    print(" [2] Configurar quantidade de follows diarias e intervalos")
    print(" [3] Analisar contas")
    print(" [4] Seguir usuários")


def obter_opcao_desejada():
    opcao = input("Digite a opção desejada e pressione ENTER: ")
    return opcao.strip()


# Fluxo principal do programa
exibir_menu()
opcao = obter_opcao_desejada()

if opcao == "1":
    print("Configurando coordenadas...")
    configura_coordenadas()
elif opcao == "2":
    print("Configurando parametros...")
    configura_parametros()
elif opcao == "3":
    print("Analisando contas...")
    analisa_contas()
elif opcao == "4":
    print("Seguindo usuários...")
    segue_perfil()
else:
    print("Opção inválida. Tente novamente.")