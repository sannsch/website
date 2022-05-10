from flask import Flask, request, render_template, redirect, flash
from test_model import waiting_num, store_ticket_num, get_number
import os

app = Flask(__name__)
app.secret_key = 'the random string'
current_num = 30

@app.route('/')
def home():
    return render_template('test_index.html')


places = ['post', 'coop']


@app.route('/add_place', methods=['POST'])
def add_place():
    place = request.form['place']
    if place in places:
        return render_template('view.html')
    else:
        flash('Butiken du har valt finns inte i listan för tillgängliga butiker')
        return render_template('test_index.html')

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    ticket_num = request.form['ticket_num']
    store_ticket_num(ticket_num)
    return redirect('/show_ticket')

@app.route('/increment_num')
def increment_num():
    global current_num
    current_num += 1

@app.route('/show_ticket')
def show_ticket():
    your_number =get_number()

    waiting = waiting_num(your_number, current_num)
    return render_template('ticket_page.html',your_number=your_number, current=current_num, waiting=waiting)


if __name__ == '__main__':
    app.run(debug=True)
