from flask import Flask
from flask_jwt_extended import JWTManager
from config import JWT_SECRET_KEY
from flask_restx import Api, Resource
from view.view_member import viewNS

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY['SECRET_KEY']

jwtmanager = JWTManager(app)

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