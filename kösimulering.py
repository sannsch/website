import requests
from random import randint
import time



def dino(y=30):
    for i in range(0,50):
        response = requests.get(f"http://127.0.0.1:5000/show_ticket?current_num={int(y)}&add=on")
        y += 1
        time.sleep(10)

dino()



