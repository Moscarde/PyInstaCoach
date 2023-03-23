from modules.json_manipulation import *
from modules.print_color import *

path_accounts_list = "resources/accounts_list.json"

# Check if account list exists and shows data
def check_accounts():
    if json_check(path_accounts_list):
        accounts_list = json_read(path_accounts_list)
        quant = 0
        for account in accounts_list:
            if account["Status"] == "Followed":
                quant += 1
        followed_accounts = quant
        not_followed_accounts = len(accounts_list) - followed_accounts
        if not_followed_accounts == 0:
            print_red("Lista de contas vazia")
            return False
        print("Lista de contas carregada")
        print("Existem", followed_accounts, "contas ja seguidas")
        print("Existem", not_followed_accounts, "contas ainda nao seguidas. *Porém podem conter erros*")

    else:
        print_red("Lista de contas vazia")
        return False