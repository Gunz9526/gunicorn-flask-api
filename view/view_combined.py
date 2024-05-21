from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource

from controller.controller_board import BoardController
from controller.controller_comment import CommentController


combined_namespace = Namespace(
    name = 'CombinedView',
    description = '게시판 엔드포인트',
    )

board_controller_object = BoardController()
comment_controller_object = CommentController()


@combined_namespace.route('/select_board/<int:combined_type>')
class BoardAllSelect(Resource):
    @jwt_required
    # @combined_namespace.expect()
    def get(self, combined_type):
        return board_controller_object.get_board(combined_type)      
    
@combined_namespace.route('/select_content/<int:combined_type>')
class ContentSelect(Resource):
    def get(self):
        pass


@combined_namespace.route('/update_content')
class ContentUpdate(Resource):
    def patch(self):
        pass

@combined_namespace.route('/delete_content')
class ContentDelete(Resource):
    def delete(self):
        pass

@combined_namespace.route('/insert_content')
class ContentInsert(Resource):
    def post(self):
        pass

@combined_namespace.route('/select_comment')
class CommentSelect(Resource):
    def get(self):
        pass

@combined_namespace.route('/insert_comment')
class CommentInsert(Resource):
    def post(self):
        pass

@combined_namespace.route('update_comment')
class CommentUpdate(Resource):
    def patch(self):
        pass

@combined_namespace.route('/delete_comment')
class CommentDelete(Resource):
    def delete(self):
        pass

@combined_namespace.route('/insert_nested_comment')
class NestedCommentInsert(Resource):
    def post(self):
        pass
