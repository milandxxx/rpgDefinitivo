from combat.combat import calcular_daño

def pvp_attack(p1, p2):
    dmg = calcular_daño(p1.atk, 50, p2.defense)
    p2.hp -= dmg
    return dmg
