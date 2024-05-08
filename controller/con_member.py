from app import db
from flask import Flask
from model.model_member import MemberModel



from model.model_member import MemberModel

class Member:
    def __init__(self):
        pass

    def convert_data(array):
        pass

    def login(self, userID, password):
        result = db.session.execute(self.db.select(MemberModel).filter_by(id = userID, pw = password).first())
        return result
    
    def test(self):
        pass

    def show_member_info(userNum):
        pass

    def join_memeber(array):
        return MemberModel.join_members(array)

    def find_password():
        pass

    def edit_info(userNum, array):
        pass

    def discard_info(userNum):
        pass