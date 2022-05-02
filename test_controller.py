from flask import Flask, request, render_template, flash
from test_model import waiting_num
import os

app = Flask(__name__)
app.secret_key = 'the random string'


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
    return render_template('ticket_page.html', variable= ticket_num)


@app.route('/show_ticket')
def show_ticket():
    current_num = '342'
    return render_template('ticket_page.html',cnummer=current_num)


if __name__ == '__main__':
    app.run(debug=True)
