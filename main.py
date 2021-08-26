from os.path import dirname, join
from uuid import uuid4

from flask import Flask, render_template, request, make_response, url_for
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.flaskenv'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mystery'
socketio = SocketIO(app)


@app.route('/')
def index():
    resp = make_response(render_template('index.html'))

    if not request.cookies.get('uuid'):
        resp.set_cookie('uuid', str(uuid4()))

    if not request.cookies.get('nick'):
        resp.set_cookie('nick', 'Player')
    
    return resp


@app.route('/set-nick', methods=['POST'])
def set_nick():
    if request.is_json:
        data = request.get_json()

        resp = make_response(('', 204))
        resp.set_cookie('nick', data['nick'])

        return resp
    else:
        return '', 400


@socketio.on('send-msg', namespace="/chat")
def handle_event(arg):
    emit('receive-msg', 
         {'text': arg, 'nick': request.cookies.get('nick')}, 
         broadcast=True)


# @socketio.

if __name__=='__main__':
    socketio.run(app)