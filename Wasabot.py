import pyautogui,webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+524433650253")
sleep(10)

pyautogui.typewrite("Hola como estas?")
pyautogui.press("Enter")