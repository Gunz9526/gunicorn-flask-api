from app import db
from model.model_board import BoardModel
from model.model_comment import CommentModel

class CommentController:
    def select_all_comment(self, board_num, limits=10):
        pass

    def insert_comment(self, content, id):
        pass

    def update_comment(self, content, id, comment_num):
        pass

    def delete_comment(self, id, comment_num):
        pass

    def insert_nested_comment(self, comment_num, content, id):
        pass
        