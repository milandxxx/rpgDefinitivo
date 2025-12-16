from flask_jwt_extended import create_access_token
from db import get_db

def register(username, password):
    db = get_db()
    c = db.cursor()
    c.execute(
        'INSERT INTO users (username,password,level,exp,fruit) VALUES (?,?,1,0,NULL)',
        (username, password)
    )
    db.commit()
    db.close()

def login(username, password):
    db = get_db()
    c = db.cursor()
    c.execute(
        'SELECT * FROM users WHERE username=? AND password=?',
        (username, password)
    )
    user = c.fetchone()
    db.close()
    if user:
        return create_access_token(identity=username)
    return None
