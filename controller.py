import requests

from flask import Flask, request, render_template, redirect, flash, jsonify
from model import waiting_num, store_ticket_num, get_number#, store_in_dictionary, save_dictionary, get_dictionary, load
import time


app = Flask(__name__)
app.secret_key = 'the random string'


@app.route('/')
def home():
    return render_template('place.html')


places = ['postnord', 'coop',  ]



@app.route('/add_place', methods=['POST'])
def add_place():
    place = request.form['place']
    if place in places:
        return render_template('add_ticket.html')
    else:
        flash('Butiken du har valt finns inte i listan för tillgängliga butiker')
        return render_template('place.html')


@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    ticket_num = request.form['ticket_num']
    store_ticket_num(ticket_num)
    return redirect('/show_ticket')


@app.route('/show_ticket')

def show_ticket():
    your_number =get_number()
    result = jsonify(time.time())
    print (result)

    
    # waiting = waiting_num(your_number, current_num)
    return render_template('ticket_page.html',your_number=your_number, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


