from termcolor import colored

def print_menu(texto):
    print(colored(texto, "cyan"))

def print_erro(texto):
    print(colored(texto, "light_red", "on_white"))

def print_seguiu(texto):
    print(colored(texto, "light_green"))

def print_nao_seguiu(texto):
    print(colored(texto, "light_blue"))

#black, red, green, yellow, blue, magenta, cyan, 
# white, light_grey, dark_grey, light_red, 
# light_green, light_yellow, light_blue, 
# light_magenta, light_cyan.