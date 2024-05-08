import os
from flask import Flask
from flask_jwt_extended import JWTManager

from flask_bcrypt import Bcrypt
from config import JWT_SECRET_KEY, db_file
from flask_restx import Api, Resource
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY['SECRET_KEY']
mybcrypt = Bcrypt(app)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()


jwtmanager = JWTManager(app)

from view.view_member import viewNS

api = Api(
    app,
    version='1.0',
    title='API 문서',
    description='Swagger 문서',
    doc="/api-docs")

api.add_namespace(viewNS, '/view')

# from view.view_member import *

if __name__ == '__main__':
    app.run(debug=True)