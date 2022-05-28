import requests
from random import randint
import time


import requests
import time



def dino():
    for i in range(1,50):

        response = requests.get(f"http://127.0.0.1:5000/show_ticket?key=beep&value={i}")


        time.sleep(10)

dino()
