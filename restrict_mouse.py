import pyautogui
import keyboard

pyautogui.FAILSAFE = False
rangex_s, rangey_s = 438, 80
wide, height = 1400, 800
rangex_f, rangey_f = rangex_s + wide, rangey_s + height
pyautogui.moveTo(rangex_f/2,rangey_f/2)

print('qを押すと終了します')
# pygame.init()
# l_m,m_m,r_m = pygame.mouse.get_pressed()

try:
    while True:
        x,y = pyautogui.position()
        position = 'X:'+str(x).rjust(4) + ' Y:'+str(y).rjust(4)
        print(position,end='')
        print('\b' * (len(position)),end='',flush=True)
        
        #mouse_pressed = pygame.mouse.get_pressed()
        # print('\b'*len(str(r_m)),end='',flush=True)
        
        if y > rangey_f: 
            #pyautogui.move(0,-100,duration=0.25)
            pyautogui.mouseUp(button="right")
            pyautogui.mouseUp(button="left")
            pyautogui.move(0,-100,duration=0.25)
        if y < rangey_s: 
            pyautogui.mouseUp(button="right")
            pyautogui.mouseUp(button="left")
            pyautogui.move(0,100,duration=0.25)
            #pyautogui.mouseUp(x,rangey_s+100,duration=0.25,button="right")
        if x > rangex_f: 
            pyautogui.mouseUp(button="right")
            pyautogui.mouseUp(button="left")
            pyautogui.move(-100,0,duration=0.25)
        if x < rangex_s: 
            pyautogui.mouseUp(button="right")
            pyautogui.mouseUp(button="left")
            pyautogui.move(100,0,duration=0.25)
        if keyboard.is_pressed("q"):
            exit()

except KeyboardInterrupt:
    print('\n終了')



