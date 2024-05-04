from flask import jsonify, request
from flask_restx import Resource, Namespace, Api, fields
from flask_jwt_extended import jwt_required

from controller.con_member import Member as MemberController

viewNS = Namespace(
    name = 'View',
    description='각 기능의 엔드포인트',
    )

count = 1
memberModel = viewNS.model('회원정보', {
    'user_num': fields.Integer(description='유저 고유 번호', required=True, example="3")
})
authModel = viewNS.model('인증', {
    'id': fields.String(description='아이디', required=True, example="test"),
    'password': fields.String(description='비밀번호', required=True, example="test")
})
@viewNS.route('/member')
class Member(Resource):
    @viewNS.expect(memberModel)
    def get(self):
        """회원 정보 조회"""
        userNum = request.form['user_num']
        MemberController.show_member_info(userNum)
    
    @viewNS.expect(memberModel)
    def delete(self):
        """회원 탈퇴"""
        userNum = request.form['user_num']
        userToken = request.form['user_token']
        MemberController.discard_info(userNum, userToken)
        return { 'user_num' : userNum, 'result' : 'success' }

    @viewNS.expect(viewNS.model('회원 가입', {'array': fields.String(description='Dict 형식의 정보 추가 항목 배열')}))
    def post(self):
        """회원가입"""
        global count
        array = request.form['array']
        array.to_dict()

        MemberController.join_memeber(array)
        count += 1
        return { 'user_num' : count , 'data' : array }

    @viewNS.expect(viewNS.inherit('회원 정보 수정', memberModel, { 'array': fields.String(description='Dict 형식의 정보 수정 항목 배열')}))
    def patch(self):
        """회원 정보 수정"""
        userNum = request.form['user_num']
        array = request.form['array']
        array.to_dict() 
        MemberController.edit_info(userNum, array)
        return { 'user_num' : userNum, 'data' : array }


@viewNS.route('/auth')
class Auth(Resource):
    # def get(self):              
    #     """회원 정보 조회"""
    #     array = request.form['info_array']
    #     test = MemberController.join_memeber(array)
    #     print(test)
    #     return { 'test' : test }

    @viewNS.expect(authModel)
    def patch(self):
        """로그인"""
        userID = request.json.get['id']
        password = request.json.get['password']
        result = MemberController.login(userID, password)
        if result == False:
            return { 'result' : 'failed', 'reason' : 'mismatched member info '}
        else:
            return {'result' : 'success', 'value' : result['access_token']}

    # @app.route('/join')
    # def join():
    #     return 'join_member'

    # @app.route('/findpw')
    # def findpw():
    #     return 'find_member_password'

    # @app.route('/edit')
    # @jwt_required(refresh=True)
    # def editinfo():
    #     return 'edit_member_info'

    # @app.route('/discard')
    # @jwt_required(refresh=True)
    # def discard():
    #     return 'discard_member_info'