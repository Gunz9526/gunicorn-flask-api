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

memeber_info_nested = viewNS.model(
    "array_nested",
    {
        'id': fields.String(required=True, description='ID', default='test'),
        'pw': fields.String(required=True, description='Password', default='test'),
        'email': fields.String(required=True, description='Email', default='test@test.com'),
    },
)

member_info = viewNS.model(
    "array",
    {
        "array": fields.Nested(memeber_info_nested),
    },
)

authModel = viewNS.model('인증', {
    'id': fields.String(description='아이디', required=True, example="test"),
    'password': fields.String(description='비밀번호', required=True, example="test")
})
@viewNS.route('/member')
class Member(Resource):
    @viewNS.expect(memberModel)
    def get(self):
        """회원 정보 조회"""
        userNum = request.get['user_num'].json()
        MemberController.show_member_info(userNum)
    
    @viewNS.expect(memberModel)
    def delete(self):
        """회원 탈퇴"""
        userNum = request.get['user_num'].json()
        userToken = request.get['user_token'].json()
        MemberController.discard_info(userNum, userToken)
        return { 'user_num' : userNum, 'result' : 'success' }

    @viewNS.expect(viewNS.model('회원 가입', member_info))
    def post(self):
        """회원가입"""
        array = request.json['array']
        print(array)
        member_con_object = MemberController()
        MemberController.join_memeber(member_con_object, array)
        return { 'id' : array['id'] , 'pw' : array }

    @viewNS.expect(viewNS.inherit('회원 정보 수정', memberModel, {'array': fields.String(description='Json 형식의 정보 추가 항목 배열')}))
    def patch(self):
        """회원 정보 수정"""
        userNum = request.json['user_num']
        # print(type(request.json))
        # print(userNum)

        array = request.json['array']
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
        user_id = request.json['id']
        password = request.json['password']
        

        ##########
        # @staticmethod 추가
        # result = MemberController.login(user_array['id'], user_array['password'])

        # # vsy
        
        # memObj = MemberController()
        # result = MemberController.login(memObj ,user_array['id'], user_array['password'])

        # # vs

        Memberobj = MemberController()
        result = Memberobj.login(user_id, password)

        ##########
        #print(result)
        if result == None:
            return { 'result' : 'failed', 'reason' : 'mismatched member info ' }
        else:
            return { 'result' : 'success', 'access_token' : result['access_token'], 'refresh_token' : result['refresh_token'] }

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