from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required

from controller.con_member import Member as MemberController

viewNS = Namespace(
    name = 'View',
    description='각 기능의 엔드포인트',
    )

memberModel = viewNS.model('회원정보', {
    'user_num': fields.Integer(description='유저 고유 번호', required=True, example="1")
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

member_edit = viewNS.model(
    '회원 정보 수정',
    {
        'user_num': fields.Integer(description='아이디', required=True),
        'pw': fields.String(description='비밀번호'),
        'email': fields.String(description='이메일')
    }
)

authModel = viewNS.model('인증', {
    'id': fields.String(description='아이디', required=True, example="test"),
    'password': fields.String(description='비밀번호', required=True, example="test")
})

password_model = viewNS.model('비밀번호 찾기', {
    'id': fields.String(description='아이디', required=True, example="test"),
    'email': fields.String(description='아이디', required=True, example="test@test.com"),
    'pw': fields.String(description='새로운 비밀번호', required=True, example="test"),
    }
)

@viewNS.route('/member')
class Member(Resource):
    @jwt_required
    @viewNS.expect(memberModel)
    def delete(self):
        """회원 탈퇴"""
        user_num = request.json['user_num']
        # userToken = request.json['access_token']
        member_con_object = MemberController()
        member_con_object.discard_info(user_num)
        return { 'user_num' : user_num, 'result' : 'success' }

    @viewNS.expect(viewNS.model('회원 가입', member_info))
    def post(self):
        """회원가입"""
        array = request.json['array']
        print(array)
        member_con_object = MemberController()
        MemberController.join_memeber(member_con_object, array)
        return { 'data' : array }

    @jwt_required
    @viewNS.expect(member_edit)
    def patch(self):
        """회원 정보 수정"""
        user_num = request.json['user_num']
        pw = request.json['pw']
        email = request.json['email']
        member_con_object = MemberController()
        MemberController.edit_info(member_con_object, user_num, pw, email)
        return { 'user_num' : user_num, 'pw': pw, 'email': email }


@viewNS.route('/auth')
class Auth(Resource):
    @viewNS.expect('비밀번호 찾기',password_model)
    def post(self):
        """비밀번호 찾기"""
        user_id = request.json['id']
        user_email = request.json['email']
        new_password = request.json['pw']
        member_con_object = MemberController()
        result = member_con_object.find_password(user_id, user_email, new_password)
        return { 'result' : result }

    @viewNS.expect(authModel)
    def patch(self):
        """로그인"""
        user_id = request.json['id']
        password = request.json['password']
        ###############################################################################################
        # @staticmethod 추가
        # result = MemberController.login(user_array['id'], user_array['password'])
        #
        # # vs
        #
        # memObj = MemberController()
        # result = MemberController.login(memObj ,user_array['id'], user_array['password'])
        #
        # # vs
        #
        member_obj = MemberController()
        result = member_obj.member_login(user_id, password)
        #############################################################################################
        #print(result)
        if result is None:
            return { 'result' : 'failed', 'reason' : 'mismatched member info ' }
        else:
            return { 'result' : 'success', 'access_token' : result[0], 'refresh_token' : result[1] }
        