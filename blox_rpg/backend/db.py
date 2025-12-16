import sqlite3

def get_db():
    return sqlite3.connect('game.db')

def init_db():
    db = get_db()
    c = db.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        level INTEGER,
        exp INTEGER,
        hp INTEGER,
        fruit TEXT
    )
    ''')
    db.commit()
    db.close()
