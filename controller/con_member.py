from flask_jwt_extended import create_access_token, create_refresh_token

from app import db, mybcrypt
from model.model_member import MemberModel


class MemberController:
    def __init__(self):
        pass

    def create_token(self, user_id):
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)
        return (access_token, refresh_token)

    def member_login(self, user_id, password):
        # print(password, hashed_password)
        result = db.session.execute(db.select(MemberModel).filter_by(id=user_id)).scalars().first()
        if result is not None:
            verify = mybcrypt.check_password_hash(result.password, password)
            if verify is True:
                return self.create_token(user_id)
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
        result = db.session.execute(db.select(MemberModel).filter_by(user_num=user_num)).first()
        result.password = hashed_password
        result.email = email
        result.verified = True
        db.session.commit()

    def discard_info(self, user_num):
        discard = db.session.execute(db.select(MemberModel).filter_by(user_num=user_num))
        discard = discard.scalars().first()
        db.session.delete(discard)
        db.session.commit()
