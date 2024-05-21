from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource

from controller.controller_board import BoardController


board_namespace = Namespace(
    name = 'BoardView',
    description = '게시판 엔드포인트',
    )

board_controller_object = BoardController()

@board_namespace.route('/select_board/<int:board_type>')
class BoardSelect(Resource):
    @jwt_required
    # @board_namespace.expect()
    def get(self, board_type):
        return board_controller_object.get_board(board_type)

@board_namespace.route('/select_content/<int:board_num>')
class ContentSelect(Resource):
    def get(self, board_num):
        result = board_controller_object.select_content(board_num)
        return result

@board_namespace.route('/update_content')
class ContentUpdate(Resource):
    def patch(self):
        content_num = request.json['content_num']
        writer = request.json['user_id']
        content = request.json['content']
        title = request.json['title']
        result = board_controller_object.update_content(content_num, title, content, writer)
        if result is not None:
            return result
        else:
            return {'result': 'failed'}

@board_namespace.route('/delete_content')
class ContentDelete(Resource):
    def delete(self):
        content_num = request.json['content_num']
        writer = request.json['user_id']
        result = board_controller_object.delete_content(content_num, writer)
        if result is not None:
            return result
        else:
            return {'result': 'failed'}

@board_namespace.route('/insert_content')
class ContentInsert(Resource):
    def post(self):
        title = request.json['title']
        content = request.json['content']
        writer = request.json['user_id']
        result = board_controller_object.insert_content(title, content, writer)
        if result is not None:
            return result
        else:
            return {'result': 'failed'}
