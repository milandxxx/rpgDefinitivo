from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from flask_socketio import SocketIO
import auth, game, multiplayer, db

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret123'
CORS(app)

jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins='*')

db.init_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    auth.register(data['username'], data['password'])
    return jsonify({'status': 'ok'})

@app.route('/login', methods=['POST'])
def login():
    token = auth.login(request.json['username'], request.json['password'])
    return jsonify({'token': token})

@app.route('/enemy')
@jwt_required()
def enemy():
    e = game.create_enemy()
    return jsonify(vars(e))

@socketio.on('join')
def join(data):
    players = multiplayer.join_room(data['room'], data['player'])
    socketio.emit('players', players, room=data['room'])

if __name__ == '__main__':
    socketio.run(app, debug=True)
