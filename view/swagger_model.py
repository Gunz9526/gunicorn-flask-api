
from flask_restx import fields
from view.view_member import viewNS

class SwaggerModel:
    memberModel = viewNS.model('회원정보', {
        'user_num': fields.Integer(description='유저 고유 번호', required=True, example="1")
    })

    memeber_info_nested = viewNS.model(
        "array_nested",
        {
            'id': fields.String(required=True, description='ID', default='test'),
            'password': fields.String(required=True, description='Password', default='test'),
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
            'password': fields.String(description='비밀번호'),
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
        'password': fields.String(description='새로운 비밀번호', required=True, example="test"),
        }
    )
