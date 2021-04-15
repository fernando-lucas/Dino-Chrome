""" bibliotecas nativas """
import time
import pyautogui
from PIL import ImageGrab

""" classes exclusivas """
from Scanner import scanUntil

# DEFINIÇÕES DE COR
#Esta é a cor do Dino, também usada por Obstáculos.
COLOR_DINOSAUR = (83, 83, 83)
DARK_COLOR_DINO = (172, 172, 172)

screen = ImageGrab.grab()

#x = scanUntil([20, 80], [0, 15], COLOR_DINOSAUR, False, 500 / 15)
#print(x)

def findGamePosition():
    pos = None
    dinoPos = None
    skipXFast = 15

    for x in range(20, screen.width, skipXFast):
        dinoPos = scanUntil([x, 80], #Start position
                            [0, skipXFast], #Skip pixels
                            COLOR_DINOSAUR, #Searching Color
                            False, #Normal mode (not inverse)
                            500 / skipXFast) #Iteration limit
        if(dinoPos):
            #return dinoPos
            break
    
    for x in range(dinoPos[0] - 50, dinoPos[0], 1):
        pos = scanUntil([x, dinoPos[1] - 2], #Start position
                            [0, 1], #Skip pixels
                            COLOR_DINOSAUR, #Searching Color
                            False, #Normal mode (not inverse)
                            100) #Iteration limit)
        if(pos):
            return pos
            break

x = findGamePosition()
pyautogui.moveTo(x)
print('Achou!')

""" Código Velho: """
if (1 > 2):
    screen = ImageGrab.grab()
    screen.save(r'print.png')

    print('Fim')

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