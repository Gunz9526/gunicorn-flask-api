from flask import Flask
from flask_jwt_extended import JWTManager
from config import JWT_SECRET_KEY

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY['SECRET_KEY']

jwtmanager = JWTManager(app)

@app.route('/')
def index():
    return 'gunicorn'

from view.view_member import *

if __name__ == '__main__':
    app.run(debug=True) 