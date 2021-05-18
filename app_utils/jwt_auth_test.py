import jwt
import datetime
from django.conf import settings

model_key = settings.SECRET_KEY

def create_token(payload, timeout = 10):
    """
    :param payload: 例如：{'u_ID':1,'u_name':'aaa'}用户信息
    :param timeout: token的过期时间，默认10分钟
    :return:
    """
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes = timeout)
    result = jwt.encode(payload = payload, key = model_key, algorithm = "HS256", 
                        headers = headers).decode('utf-8')
    return result

def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:
    """
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, model_key, True)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result