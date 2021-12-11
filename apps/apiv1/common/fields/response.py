from flask_restful import fields


__user_token_info = {
    "username": fields.String,
    "token": fields.String
}

register_or_login_fields = {
    "code": fields.Integer,
    "message": fields.String,
    "data": fields.Nested(__user_token_info)
}
