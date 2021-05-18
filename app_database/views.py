"""
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from app_database.utils.jwt_auth import create_token, parse_payload
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from app_database.models import *
import hashlib
import json

# Create your views here.

# 登录
@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name = 'dispatch')
def login(request):
    response = {}
    try:
        data = json.loads(request.body)
        user = data.get('username')
        pwd = hashlib.sha256(data.get('password').encode('utf-8')).hexdigest()
        print(pwd)
        print(user)
        user_obj = All_users.objects.filter(u_ID = user, u_pass = pwd).first()
        print(user_obj)

        if not user_obj:
            response['msg'] = '用户账户或密码错误'
            response['error_num'] = -1
            return JsonResponse(response)

        token = create_token({'username': user})
        All_users.objects.filter(u_ID = user, u_pass = pwd).update(u_token = token)
        response['token'] = token
        response['msg'] = 'success'
        response['error_num'] = 0  
        
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# 修改密码（常规）
@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name = 'dispatch')
def edit_pass_normal(request):
    response = {}
    try:
        data = json.loads(request.body)
        pwd = hashlib.sha256(data.get('old_password').encode('utf-8')).hexdigest()
        user_obj = All_users.objects.filter(u_ID = data.get('u_ID'), u_pass = pwd).first()

        if(user_obj):
            new_pwd = hashlib.sha256(data.get('new_password').encode('utf-8')).hexdigest()
            All_users.objects.filter(pk = user_obj.pk).update(u_pass = new_pwd)
        else:
            response['error_num'] = -1
            response['msg'] = '原密码错误'
            return JsonResponse(response)

        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

# 修改密码（初次）
@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name = 'dispatch')
def edit_pass_init(request):
    response = {}
    try:
        data = json.loads(request.body)
        pwd = hashlib.sha256(data.get('u_pass').encode('utf-8')).hexdigest()
        user_obj = All_users.objects.filter(u_ID = data.get('u_ID')).first()
        All_users.objects.filter(pk = user_obj.pk).update(u_pass = pwd)
        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# 登录
class UserLogin(APIView):
    response = {}
    def get(self, request):
        '''
        :params: request
        :return: json
        '''
        return JsonResponse(response)

    def post(self, request):
        '''
        :params: request
        :return: json
        '''

        try:
            data = json.loads(request.body)
            user = data.get('username')
            pwd = hashlib.sha256(data.get('password').encode('utf-8')).hexdigest()
            user_obj = All_users.objects.filter(u_ID = user, u_pass = pwd).first()

            if not user_obj:
                response['msg'] = '学号或工号错误！'
                response['error_num'] = 401
                return JsonResponse(response)


"""