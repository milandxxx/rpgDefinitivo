from flask import Blueprint, jsonify, request
from models import Player
from fruits.fruit_manager import FruitManager

fruit_bp = Blueprint('fruits', __name__)

player = Player('Jugador')
fruit_manager = FruitManager(player)

@fruit_bp.route('/fruits/roll', methods=['POST'])
def roll_fruit():
    fruit = fruit_manager.roll_fruit()
    return jsonify({'fruit': fruit})

@fruit_bp.route('/fruits/eat', methods=['POST'])
def eat_fruit():
    fruit = request.json['fruit']
    return jsonify({'success': fruit_manager.eat_fruit(fruit)})
