import pyautogui as pag
import random
import time

print("#######-Program started-#######")

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x, y, 0.5)
    clock = time.localtime()
    current_time = time.strftime("%H:%M:%S", clock)

    print(f"{current_time} Mouse is moving now! :)")

    time.sleep(60)


