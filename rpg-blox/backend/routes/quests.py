from flask import Blueprint, jsonify, request
from models import Player
from quests.quest_manager import QuestManager

quest_bp = Blueprint('quests', __name__)

player = Player('Jugador')
quest_manager = QuestManager(player)

@quest_bp.route('/quests', methods=['GET'])
def get_quests():
    return jsonify(quest_manager.available_quests())

@quest_bp.route('/quests/start', methods=['POST'])
def start_quest():
    quest_id = request.json['quest_id']
    return jsonify({'started': quest_manager.start_quest(quest_id)})

@quest_bp.route('/quests/kill', methods=['POST'])
def kill_enemy():
    enemy = request.json['enemy']
    result = quest_manager.update_progress(enemy)
    return jsonify({'status': result})
