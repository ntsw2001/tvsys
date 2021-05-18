from django.conf import settings
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from app_utils.jwt_auth_test import parse_payload
  
 
def auth_permission_required():
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
                try:
                    authorization = request.META.get('HTTP_AUTHORIZATION', '')
                    auth = authorization.split()
                except AttributeError:
                    return JsonResponse({"code": 401, "message": "No authenticate header!"})
 
                # 用户通过API获取数据验证流程
                if not auth:
                    return JsonResponse({'error': '未获取到Authorization请求头', 'status': False})
                if auth[0].lower() != 'bearer':
                    return JsonResponse({'error': 'Authorization请求头中认证方式错误', 'status': False})
                if len(auth) == 1:
                    return JsonResponse({'error': "非法Authorization请求头", 'status': False})
                elif len(auth) > 2:
                    return JsonResponse({'error': "非法Authorization请求头", 'status': False})
                token = auth[1]
                result = parse_payload(token)
                if not result['status']:
                    return JsonResponse(result)
 
                return view_func(request, *args, **kwargs)
 
        return _wrapped_view
 
    return decorator