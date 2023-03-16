import pyautogui
import pynput
from pynput import keyboard

follow_button = '../follow_btn.png'
try:
    pyautogui.locateOnScreen(follow_button, confidence=0.8)
except:
    print('img nao encontrada')
else:
    print('img encontrada')

pyautogui.locateOnScreen(follow_button, confidence=0.8)