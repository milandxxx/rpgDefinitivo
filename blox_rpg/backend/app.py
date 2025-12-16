from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_socketio import SocketIO
import db, auth, game, multiplayer

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecret'
CORS(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins='*')

db.init_db()

@app.route('/register', methods=['POST'])
def register():
    auth.register(request.json['username'], request.json['password'])
    return jsonify(ok=True)

@app.route('/login', methods=['POST'])
def login():
    token = auth.login(request.json['username'], request.json['password'])
    return jsonify(token=token)

@app.route('/fruit', methods=['POST'])
@jwt_required()
def fruit():
    return jsonify(fruit=game.random_fruit())

@socketio.on('join')
def join(data):
    players = multiplayer.join(data['room'], data['user'])
    socketio.emit('players', players, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
