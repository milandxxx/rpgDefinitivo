def calcular_daño(atk, skill_dmg, defensa):
    daño = atk + skill_dmg - defensa
    return max(1, int(daño))
