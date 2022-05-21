
import requests
import time



def dino():
    for i in range(0,50):

        response = requests.get(f"http://127.0.0.1:5000/show_ticket?key=4&value={i}")
        
        # y += 1
        

        time.sleep(10)

dino()
