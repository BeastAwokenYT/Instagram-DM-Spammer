import pyautogui, time, sleep
time.sleep(5)
f = open ("test", 'r')
for word in f:
       pyautogui.typewrite(word)
       pyautogui.press("enter") 