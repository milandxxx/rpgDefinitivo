from flask import Flask
from routes.quests import quest_bp

app = Flask(__name__)
app.register_blueprint(quest_bp)

if __name__ == "__main__":
    app.run(debug=True)
