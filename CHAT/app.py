from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users = []  # Lista per memorizzare gli utenti connessi

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('register')
def handle_register(username):
    if username not in users:
        users.append(username)
        emit('user_list', users, broadcast=True)  # Invia la lista degli utenti a tutti

@socketio.on('send_message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)  # Invia il messaggio a tutti

if __name__ == '__main__':
    socketio.run(app, debug=True)

