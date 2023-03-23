from termcolor import colored

#menu
def print_cyan(texto):
    print(colored(texto, "cyan"))


#erro
def print_red(texto):
    print(colored(texto, "light_red"))

#seguiu
def print_green(texto):
    print(colored(texto, "light_green"))

#nao seguiu
def print_pink(texto):
    print(colored(texto, "light_blue"))

def print_bold(texto):
    print(colored(texto, "light_blue", "on_black", ["bold", "blink"] ))

#black, red, green, yellow, blue, magenta, cyan, 
# white, light_grey, dark_grey, light_red, 
# light_green, light_yellow, light_blue, 
# light_magenta, light_cyan.