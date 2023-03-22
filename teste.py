import pyautogui
import time
from pynput import keyboard
from termcolor import colored
from tqdm import tqdm

cores =["black", "red", "green", 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey', 'dark_grey', 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan']

for cor in cores:
    print(colored(f'Essa eh a cor {cor}', f'{cor}'))

from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(1)