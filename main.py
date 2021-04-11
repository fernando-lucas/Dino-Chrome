""" Importa bibliotecas """
import time
import pyautogui
from PIL import ImageGrab

""" Espera para executar """
time.sleep(5)

screen = ImageGrab.grab()
screen.save(r'print.png')

"""Localiza o Dinossauro"""
x = pyautogui.locateOnScreen('dino.png')
y = pyautogui.locateCenterOnScreen('dino.png')
pyautogui.moveTo(y)

print('Tipo: ', type(x))
print('x: ', x)
print('Centro: ', y)

""" Inicia o Jogo """
time.sleep(5)
pyautogui.press("up")