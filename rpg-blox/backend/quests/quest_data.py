QUESTS = {
    1: [
        {
            'id': 'm1_bandits',
            'name': 'Derrota Bandidos',
            'level_min': 1,
            'level_max': 100,
            'objective': {
                'type': 'kill',
                'target': 'Bandit',
                'amount': 5
            },
            'rewards': {
                'xp': 500,
                'money': 100
            }
        }
    ],

    2: [
        {
            'id': 'm2_pirates',
            'name': 'Piratas del Mar',
            'level_min': 700,
            'level_max': 900,
            'objective': {
                'type': 'kill',
                'target': 'Pirate',
                'amount': 8
            },
            'rewards': {
                'xp': 3000,
                'money': 800
            }
        }
    ],

    4: [
        {
            'id': 'm4_ruins',
            'name': 'Ruinas Vivientes',
            'level_min': 2800,
            'objective': {
                'type': 'kill',
                'target': 'Living Ruin',
                'amount': 12
            },
            'rewards': {
                'xp': 20000,
                'money': 5000,
                'item': 'Fragmento Antiguo'
            }
        }
    ]
}
