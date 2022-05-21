import requests
from flask_socketio import SocketIO, emit
from flask import Flask, request, render_template, redirect, flash, url_for, copy_current_request_context, jsonify
from model import waiting_num, store_ticket_num, get_number#, store_in_dictionary, save_dictionary, get_dictionary, load
import time
from threading import Thread, Event


app = Flask(__name__)
app.secret_key = 'the random string'

# socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)
# 
# thread = Thread()
# thread_stop_event = Event()
# 
# def number_generator():
#     while not thread_stop_event.isSet():
#         number_current = 10
#         print(number_current)
#         socketio.emit('newnumber', {'number': number_current}, namespace='/test')
#         return number_current
#         number_current +=1
#         socketio.sleep(10)
# 
# @socketio.on('connect', namespace='/test')
# def test_connect():
#     global thread
# 
#     if not thread.is_alive():
#         thread = socketio.start_backgound_task(number_generator())
# 
# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected')

@app.route('/')
def home():
    return render_template('place.html')


places = ['post', 'coop']



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

# @app.route('/stuff', methods = ['GET'])
# def stuff():
#     return jsonify(result=time.time())


@app.route('/show_ticket', methods = ['GET'])
def show_ticket():
    your_number =get_number()
    result = jsonify(time.time())

    
    # waiting = waiting_num(your_number, current_num)
    return render_template('ticket_page.html',your_number=your_number, result=result)


if __name__ == '__main__':
    # socketio.run(app)
    app.run(debug=True, port=5000)

    #
    # key = request.args['key']
    # value = request.args['value']
    # store_in_dictionary(key,value)
    # save_dictionary()
    # current = get_dictionary()

    # key = request.args.get('key')
    # value = request.args.get('value')
    # store_in_dictionary(key, value)
    # save_dictionary()
    # current = get_dictionary()