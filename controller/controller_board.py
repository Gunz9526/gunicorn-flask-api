from app import db
from model.model_board import BoardModel

class BoardController:
    def get_board(self, board_type, access_token=None):
        result = db.session.execute(db.select(BoardModel).filter_by(board_type=board_type).order_by(BoardModel.board_num.desc()).limit(10)).scalars().fetchall()
        return result

    def insert_content(self, title, content, user_id, board_type):
        insert_data = BoardModel(title=title, content=content, writer=user_id, board_type=board_type)
        db.session.add(insert_data)
        db.session.commit()
        return {'result': 'success'}

    def select_content(self, board_num):
        result = db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalars().first()
        
        return result

    def update_content(self, board_num, user_id, title=None, content=None, access_token=None):
        # if owner_check(user_id, 1, board_num):
        #     result =  db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).first()
        #     if title is not None:
        #         result.title = title
        #     if content is not None:
        #         result.content = content
        #     db.session.commit()
        #     return True
        # else:
        #     return None
        ########################################
        if not permission_check(board_num, user_id):
            return None
        
        board = db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalar_one()
        if title is not None:
            board.title = title
        if content is not None:
            board.content = content
        db.session.commit()

        return board
        ########################################
        
        # result =  db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalar()
        # if result is not None:
        #     if result.writer == user_id:
        #         if title is not None:
        #             result.title = title
        #         if content is not None:
        #             result.content = content
        #         db.session.commit()
        #         return result # Object
        #     else:
        #         return False # None
        # else:
            return False

    def delete_content(self, board_num, user_id, access_token=None):
        try:
            ########################################
            if permission_check(board_num, user_id):
                board = db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalar_one()
                db.session.delete(board)
                db.session.commit()
                return True
            else:
                return False
            ########################################

            # result =  db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalar_one()        
            # if result is not None:
            #     if result.writer == user_id:
            #         db.session.delete(result)
            #         db.session.commit()
            #         return True
            #     else:
            #         return False
            # else:
            #     return False
        except:
            return False


def permission_check(board_num, user_id):
    result = False
    scalar =  db.session.execute(db.select(BoardModel).filter_by(board_num=board_num)).scalar_one()

    if scalar is not None and scalar.writer == user_id:
        result = True

    return result