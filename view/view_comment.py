from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from controller.controller_comment import CommentController

comment_namespace = Namespace(
    name = 'CommentView',
    description = '댓글 엔드포인트'
    )

comment_controller_object = CommentController()

@comment_namespace.route('/select_comment/<int:board_num>')
class CommentSelect(Resource):
    def get(self, board_num):
        result={}
        comment_value = comment_controller_object.select_all_comment(board_num)
        comment_count= len(comment_value)
        for i in range(comment_count):
            nested_array = comment_controller_object.select_nested_comment(comment_value[i].comment_num)
            result[i] = {'comment_num': comment_value[i].comment_num, 'content': comment_value[i].content, 'writer': comment_value[i].writer, 'regdate': comment_value[i].regdate, 'nested': nested_array, 'board_num': comment_value[i].board_num}
        return result

@comment_namespace.route('/insert_comment')
class CommentInsert(Resource):
    @comment_namespace.expect(comment_namespace.model('댓글 입력',{'board_num': fields.Integer(description='댓글 달 글 번호', example='3'), 'user_id': fields.String(descripttion="유저 아이디", example='test0'), 'content': fields.String(description="댓글 내용", example='댓글 테스트')}))
    def post(self):
        user_id = request.json['user_id']
        content = request.json['content']
        board_num = request.json['board_num']
        comment_controller_object.insert_comment(content, user_id, board_num)
        return {'result': 'success', 'content': content, 'user_id': user_id}

@comment_namespace.route('/update_comment')
class CommentUpdate(Resource):
    @comment_namespace.expect(comment_namespace.model('댓글 수정',{'comment_num': fields.Integer(description='수정 댓글 번호', example='8'), 'user_id': fields.String(descripttion="유저 아이디", example='test0'), 'content': fields.String(description='수정 댓글 내용',example='수정 테스트')}))
    def patch(self):
        comment_num = request.json['comment_num']
        content = request.json['content']
        user_id = request.json['user_id']
        result = comment_controller_object.update_comment(comment_num, content, user_id)
        if result is not None:
            return {'result': 'success', 'content': content}

@comment_namespace.route('/delete_comment')
class CommentDelete(Resource):
    @comment_namespace.expect(comment_namespace.model('댓글 삭제',{'comment_num': fields.Integer(description='지울 댓글 번호', example='8'), 'user_id': fields.String(descripttion="유저 아이디", example='test0')}))
    def delete(self):
        comment_num = request.json['comment_num']
        user_id = request.json['user_id']
        result = comment_controller_object.delete_comment(comment_num, user_id)
        if result is not None:
            comment_controller_object.delete_nested_comment(result.comment_num)
            return {'result': 'success', 'comment_num': comment_num}
        else:
            return {'result': 'failed', 'reason': 'unauthorized request'}


@comment_namespace.route('/insert_nested_comment')
class NestedCommentInsert(Resource):
    @comment_namespace.expect(comment_namespace.model('대댓글 입력',{'nested_num': fields.Integer(description='댓글 달 댓글 번호', example='8'), 'board_num': fields.Integer(description='달 글 번호', example='3'), 'user_id': fields.String(descripttion="유저 아이디", example='test0'), 'content': fields.String(description="댓글 내용", example='대댓글 테스트')}))
    def post(self):
        user_id = request.json['user_id']
        content = request.json['content']
        comment_num = request.json['nested_num']
        board_num = request.json['board_num']
        comment_controller_object.insert_nested_comment(comment_num, content, user_id, board_num)
        return {'result': 'success', 'user_id': user_id, 'content': content, 'nested': comment_num}
