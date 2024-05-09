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
        # print(password, hashed_password)
        result = db.session.execute(db.select(MemberModel).filter_by(id=userID)).scalars().first()
        if result != None:
            verify = mybcrypt.check_password_hash(result.pw, password)
            if verify == True:
                return self.createToken(userID)
            else:
                result = None
                return result
        else:
            return result
        
    
    def join_memeber(self, array):
        hashed_password = mybcrypt.generate_password_hash(array['pw']).decode('utf-8')
        info = MemberModel(id = array['id'], pw = hashed_password, email = array['email'])
        db.session.add(info)
        db.session.commit()

    def find_password(self, userID, email, password):        
        result = db.session.execute(db.select(MemberModel).filter_by(id=userID, email=email)).scalars().first()
        if result != None:
            hashed_password = mybcrypt.generate_password_hash(password).decode('utf-8')
            result.pw = hashed_password
            db.session.commit()
            return 'True'
        else:
            return 'False'



    def edit_info(self, userNum, password, email):
        hashed_password = mybcrypt.generate_password_hash(password).decode('utf-8')
        
        result = db.session.execute(db.select(MemberModel).filter_by(user_num=userNum)).first()
        result.pw = hashed_password
        result.email = email
        result.verified = True
        db.session.commit()

    def discard_info(self, userNum):
        discard = db.session.execute(db.select(MemberModel).filter_by(user_num=userNum)).scalars().first()
        db.session.delete(discard)
        db.session.commit()