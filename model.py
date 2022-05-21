import json


def waiting_num(ticket_num, current_num):
    return ticket_num - current_num

number = [0]
dictionary ={}

def store_ticket_num(ticket_num):
    number.append(ticket_num)
    return number

def store_current_num(current_num):
    current_list.append(current_num_num)
    return current

def get_number():
    copy_number = number[:]
    y_number = copy_number.pop()
    y_number_int = int(y_number)
    return y_number_int

def load():
    global dictionary
    try:
        with open('que.dat') as f:
            dictionary = json.load(f)
    except:
        dictionary = {}

def save_dictionary():
    with open('que.dat', 'w') as f:
        json.dump(dictionary, f)

def store_in_dictionary(key, value,):
    dictionary[key] = [dictionary[key], value]


def get_dictionary():
    current = dictionary.get(value, default=None)
    return current
            