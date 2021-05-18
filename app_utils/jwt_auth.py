import jwt
import time
from django.conf import settings
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from app_database.models import All_users

def generate_jwt(user_obj):
    '''生成JWT'''
    timestamp = int(time.time()) + 60*30*24 # 单位：秒
    # jwt.encode返回bytes类型，因而需要解码
    return jwt.encode({"userid": user_obj.pk, "exp": timestamp}, settings.SECRET_KEY).decode("utf-8")


class JWTAuthentication(BaseAuthentication):
    '''
    手动实现JWT
    Header格式：Authorization: JWT 加密的字符串
    '''

    keyword = 'jwt'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Authorization 不可用！'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Authorization 不可用！应该提供一个空格！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY)
            userid = jwt_info.get('userid')
            try:
                user = All_users.objects.get(pk = userid)
                return (user, jwt_token)
            except:
                msg = "用户不存在！"
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = 'Token已过期！'
            raise exceptions.AuthenticationFailed(msg)
