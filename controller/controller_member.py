from flask_jwt_extended import create_access_token, create_refresh_token

from app import db, mybcrypt
from model.model_member import MemberModel


class MemberController:
    def create_token(self, user_id):
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)
        return ( access_token, refresh_token )

    def member_login(self, user_id, password):
        # print(password, hashed_password)
        result = db.session.execute(db.select(MemberModel).filter_by(id=user_id)).scalars().first()
        if result is not None:
            verify = mybcrypt.check_password_hash(result.password, password)
            if verify is True:
                value =  self.create_token(user_id)
                return {'permit': result.permit, 'access_token': value[0], 'refresh_token': value[1], 'user_id': result.id, 'user_num': result.user_num}
            else:
                result = None
                return result
        else:
            return result

    def join_memeber(self, array):
        hashed_password = mybcrypt.generate_password_hash(array['password']).decode('utf-8')
        info = MemberModel(id = array['id'], password = hashed_password, email = array['email'])
        db.session.add(info)
        db.session.commit()

    def find_password(self, user_id, email, password):
        result = db.session.execute(db.select(MemberModel).filter_by(id=user_id, email=email))
        result = result.scalars().first()
        if result is not None:
            hashed_password = mybcrypt.generate_password_hash(password).decode('utf-8')
            result.password = hashed_password
            db.session.commit()
            return 'True'
        else:
            return 'False'

    def edit_info(self, user_num, password, email):
        hashed_password = mybcrypt.generate_password_hash(password).decode('utf-8')
        result = db.session.execute(db.select(MemberModel).filter_by(user_num=user_num)).scalar()
        result.password = hashed_password
        result.email = email
        db.session.commit()

    def discard_info(self, user_num):
        discard = db.session.execute(db.select(MemberModel).filter_by(user_num=user_num))
        discard = discard.scalars().first()
        db.session.delete(discard)
        db.session.commit()

    def select_user_permit(self, id):
        result = db.session.execute(db.select(MemberModel).filter_by(id=id))
        result = result.scalars().first()
        if result is not None:
            return result.permit


#     # type : 
#            1 -> board, 2 -> comment
# def owner_check(user_id, types, target_num):
#     print(user_id, target_num)
#     if types == 1:
#         from model.model_board import BoardModel
#         result = db.session.execute(db.select(BoardModel).filter_by(board_num=target_num)).first()
#     elif types == 2:
#         from model.model_comment import CommentModel
#         result = db.session.execute(db.select(CommentModel).filter_by(comment_num=target_num)).first()

#     # print("uid" + str(user_id) + "result" + str(result.writer))
#     if result is not None:
#         if result.writer == user_id:
#             return True
#         else:
#             print("1번")
#             return False
#     else:
#         print("2번")
#         return None