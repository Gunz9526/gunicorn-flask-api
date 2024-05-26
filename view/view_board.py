from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from controller.controller_board import BoardController


board_namespace = Namespace(
    name = 'BoardView',
    description = '게시판 엔드포인트',
    )

board_controller_object = BoardController()

content_model = board_namespace.model('글 작성', {
    'user_id': fields.String(description='아이디', required=True, example="test0"),
    'title': fields.String(description='제목', required=True, example="제목"),
    'content': fields.String(description='내용', required=True, example="내용"),
    }
)

@board_namespace.route('/select_board/<int:board_type>')
class BoardSelect(Resource):
    # @board_namespace.expect()
    def get(self, board_type):
        result = list()
        get_board = board_controller_object.get_board(board_type)
        # 한번에 list에 넣어서 출력할 방법은 없나? Map을 써도 된다
        # result = [array.title for array in get_board]
        for objects in get_board:
            result.append([objects.board_num, objects.title, objects.writer, objects.regdate])
        return result

@board_namespace.route('/select_content/<int:board_num>')
class ContentSelect(Resource):
    def get(self, board_num):
        result = board_controller_object.select_content(board_num)
        if result is not None:
            return {'board_num': result.board_num, 'title': result.title, 'content': result.content, 'regdate': result.regdate, 'writer': result.writer}
        else:
            return {'result': 'failed', 'reason': 'board_num does not exist'}

@board_namespace.route('/update_content')
class ContentUpdate(Resource):
    @board_namespace.expect(board_namespace.model('글 수정',{'content_num': fields.Integer(description='글 번호', example='1'), 'user_id': fields.String(descripttion="유저 아이디", example='test0'), 'title': fields.String(description="제목", example='제목변경'), 'content': fields.String(description="본문", example='본문변경')}))
    def patch(self):
        content_num = request.json['content_num']
        writer = request.json['user_id']
        content = request.json['content']
        title = request.json['title']
        result = board_controller_object.update_content(content_num, writer, title, content)
        if result is not None:
            return {'num': result.board_num, 'writer': result.writer, 'title': result.title, 'content': result.content}
        else:
            return {'result': 'failed', 'reason': 'not authorized'}

@board_namespace.route('/delete_content')
class ContentDelete(Resource):
    @board_namespace.expect(board_namespace.model('글 삭제', {'content_num': fields.Integer(description="글 번호"), 'user_id': fields.String(descripttion="유저 아이디")}))
    def delete(self):
        content_num = request.json['content_num']
        writer = request.json['user_id']
        result = board_controller_object.delete_content(content_num, writer)
        if result is True:
            return {'result': 'success'}
        else:
            return {'result': 'failed'}

@board_namespace.route('/insert_content')
class ContentInsert(Resource):
    @board_namespace.expect(content_model)
    def post(self):
        title = request.json['title']
        content = request.json['content']
        writer = request.json['user_id']
        result = board_controller_object.insert_content(title, content, writer)
        if result is not None:
            return result
        else:
            return {'result': 'failed'}
