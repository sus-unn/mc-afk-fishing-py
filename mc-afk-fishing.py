import pyautogui
import time

x = pyautogui.size()[0] / 2.0274
y = pyautogui.size()[1] / 3.0594
pyautogui.click(x, y) # click 'Back to Game' button
pyautogui.mouseDown(button='right') 
