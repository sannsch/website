
import requests
from random import randint
import time



def dino(y = 16):
    for i in range(0,50):
        response = requests.get(f"http://127.0.0.1:5000/show_ticket?current={int(y)}")
        y += 1
        time.sleep(10)

dino()
