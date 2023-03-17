import pygetwindow as gw
import time

# Obtém a lista de janelas abertas
janelas_abertas = gw.getAllWindows()

# Enumera as janelas abertas e imprime cada uma com seu índice
print("Selecione uma das janelas abaixo para redimensionar:")
for i, janela in enumerate(janelas_abertas):
    print(f"[{i}] {janela.title}")

# Lê o índice da janela selecionada pelo usuário
opcao = int(input("Digite o número da janela desejada: "))

# Obtém a janela selecionada e a redimensiona
janela_selecionada = janelas_abertas[opcao]
janela_selecionada.resizeTo(800, 800)
janela_selecionada.moveTo(400, 100)

# Espera 1 segundo para que a janela tenha tempo de atualizar
time.sleep(1)
