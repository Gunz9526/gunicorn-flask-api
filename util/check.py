from app import db
from model.model_board import  BoardModel
from model.model_comment import CommentModel


def permission_check(target_num, user_id, category):
    result = False
    if category == 1:
        model = BoardModel
    else:
        model = CommentModel
    scalar =  db.session.execute(db.select(model).filter_by(board_num=target_num)).scalar_one()
    if scalar is not None and scalar.user_id == user_id:
        result = True

    return result