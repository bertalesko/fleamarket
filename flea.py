import pyscreenshot as imagegrab
import cv2
import pytesseract
import keyboard
import time
from PIL import Image, ImageEnhance, ImageFilter
import win32api, win32con
import datetime
import schedule


#zmienic nazwe na fence
nazwa = "Fence"

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)



def rob():
    box = (706,145,872,207)

    screenshot1 = imagegrab.grab(box)
    
    return screenshot1
    
    



def tesse():
  
    img = rob()
    pix = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)
    img.save('temp.jpg')
    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    # os.remove('temp.jpg')e
    print(text)
    return text


def odswiez():
    click(1838,117)
    time.sleep(.5)






def kup():
    print('jest')
    click(1760,170)
    time.sleep(.5)
    click(850,600)
    time.sleep(.5)
    now = datetime.datetime.now()
    print("kupilem : "+ now.strftime("%Y-%m-%d %H:%M:%S"))


def sprawdz():
    odswiez()
    text = tesse()
    if nazwa in text:
        kup()
    else:
        now = datetime.datetime.now()
        print("nie ma, czekam minute : "+ now.strftime("%Y-%m-%d %H:%M:%S"))
        




schedule.every(1).minutes.do(sprawdz)



while True:
    schedule.run_pending()
    time.sleep(1)

    if keyboard.is_pressed('e'):  
        break

