from PIL import Image, ImageGrab
import pyautogui
import time

def press(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(300, 415):
        for j in range(410, 563):   #here we are making a rectange to catch up the bird
            if data[i, j] < 100:    #change the values according to game screensize in your pc 
                press("down")          
                return              

#TO CHANGE THE VALUES AND SEE IF YOU ARE DOING IT RIGHT USE THE BELOW FOP LOOP TAKE SCREENSHOT OF YOUR RECTANGLE
                '''
                  for i in range(275, 325):
                     for j in range(563, 650):
                        data[i, j] = 0
        
                for i in range(250, 300):
                        for j in range(410, 563):
                            data[i, j] = 171

                 image.show()
                    break
                '''
#this one is to catch up the cactus
    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                press("up")
                return
    return

if __name__ == "__main__":
    print(">>>>>>>>>>>>The game will start in a few seconds<<<<<<<<<<<<<<<")
    time.sleep() #You can change delay as per yor preference

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            


