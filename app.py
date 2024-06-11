from flask import Flask
from flask_jwt_extended import JWTManager

from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask_sqlalchemy import  SQLAlchemy

from config import JWT_SECRET_KEY, db_file

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY['SECRET_KEY']
mybcrypt = Bcrypt(app)
CORS(app,resource={r'*':{'origins':'*'}})
db = SQLAlchemy()
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()


from view.view_member import member_namespace
from view.view_board import board_namespace
from view.view_comment import comment_namespace

jwtmanager = JWTManager(app)


authorizations = {'bearer_auth': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'Authorization'
    }}

api = Api(
    app,
    version='1.0',
    title='API 문서',
    description='Swagger 문서',
    authorizations=authorizations,
    security='bearer_auth',
    doc="/api-docs")

api.add_namespace(member_namespace, '/view_member')
api.add_namespace(board_namespace, '/view_board')
api.add_namespace(comment_namespace, '/comment')


if __name__ == '__main__':
    app.run(debug=True)
