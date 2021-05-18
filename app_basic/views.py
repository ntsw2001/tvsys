from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app_basic.serializers import *
from app_database.models import *
from app_utils.jwt_auth import *
from app_utils.permission import *
# from app_utils.pagination import *
import hashlib

# Create your views here.

class Login(APIView):
    '''登录'''
    throttle_scope = 'guest'

    def post(self, request):
        data = request.data
        #print(data)
        uid = data.get('u_ID')
        pwd = hashlib.sha256(data.get('u_pass').encode('utf-8')).hexdigest()
        user_obj = All_users.objects.filter(u_ID = uid, u_pass = pwd).first()

        if not user_obj:
            return Response({"code":500, "msg":"学号/工号或密码错误！"})

        token = generate_jwt(user_obj)

        return Response({"code":200,
                         "u_name":user_obj.get_user_name(),
                         "token":token
                         })


class Lend(APIView):
    '''借'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data.copy() # request.data 为不可修改的 QueryDict 对象，因此用copy()方法复制一份
        data.update({"b_user":request.user.__str__()}) # 在其中增加 u_ID 键值对

        device = data.get('b_device')
        try:
            device_obj = All_devices.objects.get(d_ID = device)
        except:
            return Response({"code":404, "msg":'设备不存在！'})

        if device_obj.get_device_status() == 0:
            return Response({"code":500, "msg":'设备已借出！'})

        serializer = RecordsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            device_obj.set_status(0)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class Retun(APIView):
    '''还'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer]
    #throttle_scope = 'user'

    def get_record_object(self, bid):
        '''搜索记录，返回记录对象'''
        try:
            return Borrow_return.objects.get(pk = bid)
        except Borrow_return.DoesNotExist:
            return Response({'code':404, 'msg':'未找到记录！'})

    def get(self, request):
        '''只获取了数据库记录视图，返回未归还记录'''
        queryset = Borrow_return_MyView.objects.filter(b_user = request.user.__str__(), r_date = None).order_by('-b_date')
        if queryset:
            # pg = GlobalPagination()
            # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
            # serializer = RecordsMyViewSerializer(instance = page_queryset, many = True)
            # return pg.get_paginated_response(data = serializer.data)
            serializer = RecordsMyViewSerializer(instance = queryset, many = True)
            return Response(serializer.data)
        else:
            return Response({"code":404, "msg":'无记录。'})

    def put(self, request, pk):
        _record = self.get_record_object(pk)
        data = request.data.copy()

        try:
            place = data.get('r_place')
            date = data.get('r_date')
        except:
            return Response({"code":500 ,"msg":'未传递归还地点或归还时间！'})

        data.update({"b_ID":None, "b_user":None, "b_device":None, "b_date":None, "b_reason":None,
                     "b_place":None, "r_assign":None})

        serializer = RecordsSerializer(_record, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            device_obj = All_devices.objects.get(d_ID = _record.get_device())
            device_obj.set_place(place)
            device_obj.set_status(1)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ModifyPass(APIView):
    '''更改密码'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data
        u_pass_new = data.get('u_pass_new')
        u_pass_old = data.get('u_pass_old')

        if u_pass_new == '123456':
            return Response({"code":403, "msg":'不允许设置密码为初始密码！'})

        try:
            u_pass_old = hashlib.sha256(u_pass_old.encode('utf-8')).hexdigest()
            user_obj = All_users.objects.get(pk = request.user.__str__(), u_pass = u_pass_old)
        except:
            return Response({"code":500, "msg":'原密码不正确！'})

        u_pass_new = hashlib.sha256(u_pass_new.encode('utf-8')).hexdigest()
        user_obj.set_pass(u_pass_new)

        return Response({"code":200, "msg":'修改成功！'})


class ResetPass(APIView):
    '''重置密码'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [Is_admin, HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        u_ID = request.data.get('u_ID')
        initial_pass = '123456'

        u_pass_new = hashlib.sha256(initial_pass.encode('utf-8')).hexdigest()
        user_obj = All_users.objects.get(u_ID = u_ID).set_pass(u_pass_new)

        return Response({"code":200, "msg":'重置成功！'})