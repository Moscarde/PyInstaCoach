from analisa_contas import analisa_contas

def exibir_menu():
    print("Bem-vindo ao nosso programa!")
    print("Escolha uma das opções abaixo:")
    print(" [1] Configurar coordenadas")
    print(" [2] Analisar contas")
    print(" [3] Seguir usuários")


def obter_opcao_desejada():
    opcao = input("Digite a opção desejada e pressione ENTER: ")
    return opcao.strip()


# Fluxo principal do programa
exibir_menu()
opcao = obter_opcao_desejada()

if opcao == '1':
    print("Configurando coordenadas...")
elif opcao == '2':
    print("Analisando contas...")
    analisa_contas()
elif opcao == '3':
    print("Seguindo usuários...")
else:
    print("Opção inválida. Tente novamente.")