from flask import Flask

from model.model_member import MemberModel

class Member:
    def __init__(self):
        pass


    def login(userID, password):
        if MemberModel.check_login(userID, password):
            return MemberModel.createToken(userID)
        else:
            return False
    
    def test(self):
        pass

    def show_member_info(userNum):
        pass

    def join_memeber(array):
        return MemberModel.join_members()

    def find_password():
        pass

    def edit_info(userNum, array):
        pass

    def discard_info(userNum):
        pass