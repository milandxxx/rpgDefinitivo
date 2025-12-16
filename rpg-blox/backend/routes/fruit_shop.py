from flask import Blueprint, jsonify, request
from fruit_shop.fruit_shop import FruitShop
from models import Player

fruit_shop_bp = Blueprint('fruit_shop', __name__)
shop = FruitShop()
player = Player('Jugador')

@fruit_shop_bp.route('/fruit-shop', methods=['GET'])
def get_shop():
    return jsonify(shop.get_stock())

@fruit_shop_bp.route('/fruit-shop/buy', methods=['POST'])
def buy():
    fruit = request.json['fruit']
    success, msg = shop.buy(player, fruit)
    return jsonify({'success': success, 'result': msg})
