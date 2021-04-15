from PIL import ImageGrab
import pyautogui

# Indexes
X = 0
Y = 1

screen = ImageGrab.grab()

def scanUntil(start, delta, matchColor, inverted, iterLimit):
    color = None
    current = None 
    iterations = 0
    pos = [start[X], start[Y]]
    
    while(not isOutOfBound(pos)):
        #pyautogui.moveTo(pos) #Move o Mouse
        color = screen.getpixel((pos[X], pos[Y]))

        if(color == matchColor):
            return pos

        pos[X] += delta[X]
        pos[Y] += delta[Y]
        iterations += 1

        if(iterations > iterLimit):
            return None

    return None

# Check if the given position is outside the Screen
# Verifique se a posição dada está fora da tela
def isOutOfBound(pos):
    if(pos[X] < 0 or pos[Y] < 0 or pos[X] >= screen.width or pos[Y] >= screen.height):
       return True
    return False