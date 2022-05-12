
import requests
from random import randint
import time



def dino(y = 16):
    for i in range(0,50):
        response = requests.get(f"http://127.0.0.1:8080/add?key={int(y)}&value=beep&add=on")
        y += 1
        time.sleep(10)

dino()
