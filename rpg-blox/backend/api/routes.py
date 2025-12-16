from flask import Blueprint, jsonify, request
from saves.save_manager import save_player, load_player

api = Blueprint('api', __name__)

@api.route('/save', methods=['POST'])
def save():
    save_player(type('Player',(object,),request.json))
    return jsonify({'status':'saved'})

@api.route('/load/<name>')
def load(name):
    return jsonify(load_player(name))
