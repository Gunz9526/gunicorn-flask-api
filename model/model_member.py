import time

from sqlalchemy import String
from app import db

from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from sqlalchemy.orm import Mapped, mapped_column

class MemberModel(db.Model):
    __tablename__ = 'member'
    user_num: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[str] = mapped_column(String(20))
    pw: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200),nullable=False)
    permit: Mapped[int] = mapped_column(nullable=False, default=0)
    create_at: Mapped[int] = mapped_column(nullable=False, default=time.time())
    update_at: Mapped[int] = mapped_column(nullable=True)

    

# class MemberModel():
#     def __init__(self):
#         pass

#     def get_member_orm(self):
#         member = Table('member', metadata, autoload=True)
#         return db
    # def createToken(userID):
    #     access_token = create_access_token(identity=userID)
    #     refresh_token = create_refresh_token(identity=userID)
        
    #     # DB 쿼리 부분
        
    #     return jsonify(access_token=access_token, refresh_token=refresh_token)
    
    # def check_tokens(token):
    #     pass
    
    # def reissueToken(accessToken, refreshToken):
    #     pass


    # def get_member_info():
    #     pass

    # def check_login(userID, user_password):
    #     hashed_password = mybcrypt.generate_password_hash(user_password).decode('utf-8') 
    #     print(userID, hashed_password)
    #     cursor.execute("""SELECT * FROM member WHERE id=(?) and pw=(?)""", (userID, hashed_password))
    #     check_data = cursor.fetchall()
    #     return check_data

    # # def find_password(input_password):
    # #     pass

    # def join_members(array): 
    #     if array == Null or array == None:
    #         return {"result" : "success"}
    #     hashed_password = mybcrypt.generate_password_hash(array['password']).decode('utf-8') 
    #     cursor.execute(f"INSERT INTO member VALUES({array['id']}, {hashed_password}, {array['name']}, 0, '1900-01-01', '1900-01-01', '1900-01-01' )")
    #     return {"result" : "success", "member" : array['name']}

    # def edit_member_info():
    #     pass

    # def discard_member_info():
    #     pass
