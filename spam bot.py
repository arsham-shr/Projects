#import pip

#def install(package):
#    if hasattr(pip, 'main'):
#        pip.main(['install', package])
#    else:
#        pip._internal.main(['install', package])

#if __name__ == '__main__':
#    install('pyautogui')

import pyautogui
import time

#pyautogui.typewrite('hello', interval=0.0001)

text = input("text: ")
times = input("times: ")
sleep = int(input("sleep: "))
time.sleep(sleep)

for i in range(int(times)):
	pyautogui.typewrite(text, interval=0.1)
	pyautogui.press('enter')