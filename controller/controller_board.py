from app import db
from model.model_board import BoardModel

class BoardController:
    def get_board(self, board_type, access_token=None):
        result = db.session.execute(db.select(BoardModel).filte_by(board_type=board_type)).scalars()
        print(type(result))

    def insert_content(self, title, content, user_id):
        insert_data = BoardModel(title=title, content=content, writer=user_id)
        db.session.add(insert_data)
        db.session.commit()
        return {'result': 'success'}

    def select_content(self, board_num):
        pass

    def update_content(self, board_num, title, content, access_token):
        pass

    def delete_content(self, board_num, access_token):
        pass

    # type : 
    #        1 -> board, 2 -> comment
    def authorization_check(self, user_num, type, target_num):
        pass