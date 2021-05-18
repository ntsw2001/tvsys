#from django.shortcuts import render
#from rest_framework.decorators import api_view
#from rest_framework import viewsets, status, generics, mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app_manage.serializers import *
from app_database.models import *
# from app_utils.pagination import *
from app_utils.jwt_auth import *
from app_utils.permission import *
import json

# Create your views here.

"""
# 用户管理视图 test1-viewsets
class UsersViewset(viewsets.ModelViewSet):
    queryset = All_users.objects.all()
    serializer_class = UsersSerializer
"""


# 用户管理视图 test2-APIView
class UsersManageViews(APIView):
    '''用户管理视图'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [Is_admin, HaveRefer]
    #throttle_scope = 'user'

    def get_user_object(self, userid):
        '''搜索用户，返回用户对象'''
        try:
            return All_users.objects.get(pk = userid)
        except All_users.DoesNotExist:
            return Response({'code':'404', 'msg':'查无此人！'})

    def get(self, request, pk = None):
        if pk:
            _user = self.get_user_object(pk)
            serializer = UsersSerializer_NoPass(_user)
            return Response(serializer.data)
        else:
            #data = request.data
            #userid = data['u_ID']
            #username = data['u_name']
            #userpass = data['u_pass']
            #userauth = data['u_auth']
            queryset = All_users.objects.all().order_by('-u_ID')

            # 分页
            # pg = GlobalPagination()
            # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
            # serializer = UsersSerializer_NoPass(instance = page_queryset, many = True)

            # return pg.get_paginated_response(data = serializer.data)
            serializer = UsersSerializer_NoPass(instance = queryset, many = True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        _user = self.get_user_object(pk)
        serializer = UsersSerializer(_user, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        _users = self.get_user_object(pk)
        _users.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


"""
# 用户管理视图 test3-generic
class UsersManageViews(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    '''用户管理视图'''

    queryset = All_users.objects.all()
    serializer_class = UsersSerializer

    def get(self, request, pk = None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""


# 设备管理视图 APIView
class DevicesManageViews(APIView):
    '''设备管理视图'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer, Is_admin]
    #throttle_scope = 'user'

    def get_device_object(self, did):
        '''搜索设备，返回设备对象'''
        try:
            return All_devices.objects.get(pk = did)
        except All_devices.DoesNotExist:
            return Response({'code':'404', 'msg':'查无此物！'})

    def get(self, request, pk = None):
        if pk:
            _device = self.get_device_object(pk)
            serializer = DevicesSerializer(_device)
            return Response(serializer.data)
        else:
            queryset = All_devices.objects.all().order_by('d_ID')

            # pg = GlobalPagination()
            # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
            # serializer = DevicesSerializer(instance = page_queryset, many = True)
            # return pg.get_paginated_response(data = serializer.data)
            serializer = DevicesSerializer(instance = queryset, many = True)
            return Response(serializer.data)


    def post(self, request):
        serializer = DevicesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        _device = self.get_device_object(pk)
        serializer = DevicesSerializer(_device, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        _device = self.get_device_object(pk)
        _device.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# 记录管理视图 APIView
class RecordsManageViews(APIView):
    '''记录管理视图'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [Is_admin, HaveRefer]
    #throttle_scope = 'user'

    def get_record_object(self, bid):
        '''搜索记录，返回记录对象'''
        try:
            return Borrow_return.objects.get(pk = bid)
        except Borrow_return.DoesNotExist:
            return Response({'code':'404', 'msg':'未找到记录！'})

    def get_recordView_object(self, bid):
        '''搜索记录视图，返回记录对象'''
        try:
            return Borrow_return_view.objects.get(pk = bid)
        except Borrow_return_view.DoesNotExist:
            return Response({'code':'404', 'msg':'未找到记录！'})

    def get(self, request, pk = None):
        '''只获取了数据库记录视图'''
        if pk:
            _record = self.get_recordView_object(pk)
            serializer = RecordsViewSerializer(_record)
            #print(serializer.data)
            return Response(serializer.data)
        else:
            queryset = Borrow_return_view.objects.all().order_by('-b_date')
            # pg = GlobalPagination()
            # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
            # serializer = RecordsViewSerializer(instance = page_queryset, many = True)

            # return pg.get_paginated_response(data = serializer.data)
            serializer = RecordsViewSerializer(instance = queryset, many = True)
            return Response(serializer.data)

    def post(self, request):
        serializer = RecordsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        _record = self.get_record_object(pk)
        serializer = RecordsSerializer(_record, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        _record = self.get_record_object(pk)
        _record.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)