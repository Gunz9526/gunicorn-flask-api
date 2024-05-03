from os import sysconf
from flask import jsonify
from sqlalchemy import *
from flask_jwt_extended import create_access_token, create_refresh_token

import sqlite3
import bcrypt

# def fileopen():
#     line_count = 0
#     with open("db.txt", "w") as f:
#         data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
#     return data

con = sqlite3.connect("./database.db")
cursor = con.cursor()

class MemberModel:
    def __init__(self):
        pass

    def createToken(userID):
        access_token = create_access_token(identity=userID)
        refresh_token = create_refresh_token(identity=userID)
        
        # DB 쿼리 부분
        
        return jsonify(access_token=access_token, refresh_token=refresh_token)
    
    def reissueToken(accessToken, refreshToken):
        pass

    def get_member_info():
        pass

    def check_login(userID, password):
        hashed_password = bcrypt.hashpw(password=password, salt=bcrypt.gensalt())
        cursor.excute(f"SELECT * FROM member WHERE id={userID} and pw={hashed_password}")
        check_data = cursor.fetchall()
        if check_data != Null:
            return check_data
        else:
            return False

    def check_tokens(token):
        pass

    def find_password(input_password):
        pass

    def join_members(array): 
        if array == Null or array == None:
            return {"result" : "success"}
        hashed_password = bcrypt.hashpw(password=array['password'], salt=bcrypt.gensalt())
        cursor.excute(f"INSERT INTO member VALUES({array['id']}, {hashed_password}, {array['name']}, 0, '1900-01-01', '1900-01-01', '1900-01-01' )")
        return {"result" : "success", "member" : array['name']}

    def edit_member_info():
        pass

    def discard_member_info():
        pass
