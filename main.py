import pyautogui as pt
import time

limit = input("Enter Limit:")
message = input("Enter Message:")
i = 0
time.slepp(3)

while i <int(limit):
  pt.typewrite(message)
  # the message is written where -
  # the cursor belongs

pt.press(enter)

l+=1
