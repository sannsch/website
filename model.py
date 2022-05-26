import json
from random import randint

def waiting_num(ticket_num, current_num):
    return ticket_num - current_num

number = [0]
current = 0

def store_ticket_num(ticket_num):
    number.append(ticket_num)
    return number


def get_number():
    copy_number = number[:]
    y_number = copy_number.pop()
    y_number_int = int(y_number)
    return y_number_int


def create_current_num():
    global current
    current_num = randint(3, 20)
    current =current_num
    return current

def get_current_num():
    global current
    current +=1
    return current


# def load():
#     global dictionary
#     try:
#         with open('que.dat') as f:
#             dictionary = json.load(f)
#     except:
#         dictionary = {}
#
# def save_dictionary():
#     with open('que.dat', 'w') as f:
#         json.dump(dictionary, f)
#
# def store_in_dictionary(key, value,):
#     dictionary[key] = [dictionary[key], value]
#
#
# def get_dictionary():
#     current = dictionary.get(value, default=None)
#     return current
#
#


    