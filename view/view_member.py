from flask import request
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required

from controller.controller_member import MemberController

member_namespace = Namespace(
    name = 'MemberView',
    description='회원 기능의 엔드포인트',
    )

member_model = member_namespace.model('회원정보', {
        'user_num': fields.Integer(description='유저 고유 번호', required=True, example="1")
    }
)

memeber_info_nested = member_namespace.model(
    "array_nested",
    {
        'id': fields.String(required=True, description='ID', default='test'),
        'password': fields.String(required=True, description='Password', default='test'),
        'email': fields.String(required=True, description='Email', default='test@test.com'),
    },
)

member_info = member_namespace.model(
    "array",
    {
        "array": fields.Nested(memeber_info_nested),
    },
)

member_edit = member_namespace.model('회원 정보 수정', {
        'user_num': fields.Integer(description='아이디', required=True),
        'password': fields.String(description='비밀번호', example='test'),
        'email': fields.String(description='이메일', example='test3@test3.com'),
    }
)

authModel = member_namespace.model('인증', {
        'id': fields.String(description='아이디', required=True, example="test"),
        'password': fields.String(description='비밀번호', required=True, example="test")
    }
)

password_model = member_namespace.model('비밀번호 찾기', {
    'id': fields.String(description='아이디', required=True, example="test"),
    'email': fields.String(description='아이디', required=True, example="test@test.com"),
    'password': fields.String(description='새로운 비밀번호', required=True, example="test"),
    }
)

@member_namespace.route('/member/join', methods=['POST'])
class MemberJoin(Resource):
    @member_namespace.expect(member_namespace.model('회원 가입', member_info))
    def post(self):
        """회원가입"""
        array = request.json['array']
        print(array)
        member_con_object = MemberController()
        MemberController.join_memeber(member_con_object, array)
        return { 'data' : array }


@member_namespace.route('/member/edit', methods=['PATCH'])
class MemberEdit(Resource):
    @member_namespace.expect(member_namespace.model('회원 정보 수정', member_edit))
    @jwt_required()
    def patch(self):
        """회원 정보 수정"""
        user_num = request.json['user_num']
        password = request.json['password']
        email = request.json['email']
        member_con_object = MemberController()
        MemberController.edit_info(member_con_object, user_num, password, email)
        return { 'user_num' : user_num, 'password': password, 'email': email }
    

@member_namespace.route('/member/delete', methods=['DELETE'])
class MemberDelete(Resource):
    @member_namespace.expect(member_namespace.model('회원 탈퇴',member_model))
    @jwt_required()
    def delete(self):
        """회원 탈퇴"""
        user_num = request.json['user_num']
        # userToken = request.json['access_token']
        member_con_object = MemberController()
        member_con_object.discard_info(user_num)
        return { 'user_num' : user_num, 'result' : 'success' }



@member_namespace.route('/auth/find', methods=['POST'])
class AuthFind(Resource):
    @jwt_required()
    @member_namespace.expect('비밀번호 찾기',password_model)
    def post(self):
        """비밀번호 찾기"""
        user_id = request.json['id']
        user_email = request.json['email']
        new_password = request.json['password']
        member_con_object = MemberController()
        result = member_con_object.find_password(user_id, user_email, new_password)
        return { 'result' : result }


@member_namespace.route('/auth/login', methods=['POST'])
class AuthLogin(Resource):
    @member_namespace.expect(authModel)
    def post(self):
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
            return { 'result' : 'success', 'access_token' : result['access_token'], 'refresh_token' : result['refresh_token'], 'permit': result['permit'], 'user_id': result['user_id'] , 'user_num': result['user_num']}
        