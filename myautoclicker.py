import pydirectinput as pyd
import keyboard

while True:
    if keyboard.is_pressed("o"):
        pyd.rightClick()
    elif keyboard.is_pressed("p"):
        pyd.leftClick()