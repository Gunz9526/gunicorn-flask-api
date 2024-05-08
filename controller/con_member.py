from flask_jwt_extended import create_access_token, create_refresh_token
from app import db, mybcrypt
from flask import Flask
from model.model_member import MemberModel



from model.model_member import MemberModel

class Member:
    def __init__(self):
        pass

    def createToken(self, userID):
        access_token = create_access_token(identity=userID)
        refresh_token = create_refresh_token(identity=userID)
        return (access_token, refresh_token)

    def login(self, userID, password):
        hashed_password = mybcrypt.generate_password_hash(password).decode('utf-8')
        result = db.session.execute(db.select(MemberModel).filter_by(id = userID, pw = hashed_password)).first()
        if result != None:
            return self.createToken(userID)
        else:
            return result
    
    def join_memeber(self, array):
        hashed_password = mybcrypt.generate_password_hash(array['pw']).decode('utf-8')
        info = MemberModel(id = array['id'], pw = hashed_password, email = array['email'])
        db.session.add(info)
        db.session.commit()

    def find_password():
        pass

    def edit_info(userNum, array):
        # modified_info = MemberModel()
        # db.session.execute(db.)
        pass

    def discard_info(userNum):
        pass