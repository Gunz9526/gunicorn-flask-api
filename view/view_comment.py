from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource

from controller.controller_comment import CommentController

comment_namespace = Namespace(
    name = 'CommentView',
    description = '댓글 엔드포인트'
    )

comment_controller_object = CommentController()

@comment_namespace.route('/select_comment/<int:board_num>')
class CommentSelect(Resource):
    def get(self, board_num):
        return comment_controller_object.select_all_comment(board_num)

@comment_namespace.route('/insert_comment')
class CommentInsert(Resource):
    def post(self):
        writer = request.json['user_id']
        content = request.json['content']
        comment_controller_object.insert_comment(writer,content)
        return {'result': 'success', 'content': content}

@comment_namespace.route('/update_comment')
class CommentUpdate(Resource):
    def patch(self):
        comment_num = request.json['comment_num']
        content = request.json['content']
        writer = request.json['user_id']
        result = comment_controller_object.update_comment(comment_num, content, writer)
        if result is not None:
            return {'result': 'success', 'content': content}

@comment_namespace.route('/delete_comment')
class CommentDelete(Resource):
    def delete(self):
        comment_num = request.json['comment_num']
        writer = request.json['user_id']
        result = comment_controller_object.delete_comment(comment_num, writer)
        if result is not None:
            return {'result': 'success', 'comment_num': comment_num}
        else:
            return {'result': 'failed', 'reason': 'unauthorized request'}


@comment_namespace.route('/insert_nested_comment')
class NestedCommentInsert(Resource):
    def post(self):
        writer = request.json['user_id']
        content = request.json['content']
        comment_num = request.json['comment_num']
        comment_controller_object.insert_nested_comment(comment_num, content, writer)
