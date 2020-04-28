from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import time
import asyncio

time.sleep(3) 

# x,y coordinates of the pixels for each direction of the attacks
pos_topcircle = [1277, 850]
pos_leftcircle = [989, 1142]
pos_rightcircle = [1565, 1142]

# default r,g,b color of the attack pixels 
colordefault_topcircle = (158, 181, 76)
colordefault_leftcircle = (125, 160, 65)
colordefault_rightcircle = (144, 172, 76)

keyboard = Controller() # define keyboard keys

async def HitTop():
    keyboard.press('w')
    keyboard.release('w')
    print("w key pressed")

async def HitLeft():
    keyboard.press('a')
    keyboard.release('a')
    print("a key pressed")

async def HitRight():
    keyboard.press('d')
    keyboard.release('d') 
    print("d key pressed")

def main(): 
    
    while True:
        px=ImageGrab.grab().load()
        if str(px[pos_topcircle[0], pos_topcircle[1]]) != str(colordefault_topcircle):
            print("w key detected")
            asyncio.run(HitTop())
            
        if str(px[pos_leftcircle[0], pos_leftcircle[1]]) != str(colordefault_leftcircle):
            asyncio.run(HitLeft())
            print("a key detected")
            
        if str(px[pos_rightcircle[0], pos_rightcircle[1]]) != str(colordefault_rightcircle):
            asyncio.run(HitRight())
            print("d key detected")

    exit()

main()