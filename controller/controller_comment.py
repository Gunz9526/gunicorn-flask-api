import time
from app import db
from model.model_comment import CommentModel

class CommentController:
    def select_all_comment(self, board_num, limits=10):
        result =  db.session.execute(db.select(CommentModel).filter_by(board_num=board_num, nested=0).order_by(CommentModel.regdate).limit(limits)).scalars().fetchall()
        return result

    def select_nested_comment(self, nested, limits=10):
        result = db.session.execute(db.select(CommentModel).filter_by(nested=nested).limit(limits)).scalars().fetchall()
        nested_array = dict()
        for i in range(len(result)):
            if result[i].nested == 0:
                nested_array[i] = {'content': result[i].content, 'writer': result[i].writer, 'regdate': result[i].regdate, 'nested': {}, 'board_num': result[i].board_num}
            else:
                nested_array[i] = {'content': result[i].content, 'writer': result[i].writer, 'regdate': result[i].regdate, 'nested': self.select_nested_comment(result[i].comment_num), 'board_num': result[i].board_num}
        return nested_array

    def insert_comment(self, content, user_id, board_num):
        result = CommentModel(content=content, writer=user_id, board_num=board_num)
        db.session.add(result)
        db.session.commit()
        return True

    def update_comment(self, comment_num, content, user_id):
        result = db.session.execute(db.select(CommentModel).filter_by(comment_num=comment_num)).scalar_one()
        if result is not None:
            if result.writer == user_id:
                result.content = content
                db.session.commit()
                return {'result': 'success', 'value': content}
            else:
                return None
        else:
            return None

    def delete_comment(self, comment_num, user_id):
        result = db.session.execute(db.select(CommentModel).filter_by(comment_num=comment_num)).scalar()
        if result is not None:
            if result.writer == user_id:
                db.session.delete(result)
                db.session.commit()
                return True
            else:
                return None
        else:
            return None
        
    def delete_nested_comment(self, nested):
        result = db.session.execute(db.select(CommentModel).filter_by(nested=nested)).scalars()
        db.session.delete(result)
        db.session.commit()

            
    def insert_nested_comment(self, comment_num, content, user_id, board_num):
        insert_data = CommentModel(nested=comment_num, content=content, writer=user_id, board_num=board_num)
        db.session.add(insert_data)
        db.session.commit()
        return True