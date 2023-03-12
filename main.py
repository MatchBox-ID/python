import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(50)
for i in range(10):
    pyautogui.press("hii bro How are You ?")
    pyautogui.press("enter")
