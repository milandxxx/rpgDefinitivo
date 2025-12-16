def calcular_daño(atk, skill_dmg, defensa):
    daño = atk + skill_dmg - defensa
    return max(1, int(daño))

def atacar(player, enemy, weapon):
    daño = calcular_daño(player.atk, weapon['damage'], enemy.defense)
    enemy.hp -= daño
    return daño
