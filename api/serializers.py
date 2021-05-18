from rest_framework import serializers
from app_database.models import *


class UsersSerializer_NoPass(serializers.ModelSerializer):
    '''不返回密码的用户序列化'''
    class Meta:
        model = All_users
        exclude = ['u_pass']


class DevicesSerializer(serializers.Serializer):
    '''设备序列化'''
    d_ID = serializers.CharField(required = False, max_length = 12)
    d_see = serializers.IntegerField(required = False)
    d_type = serializers.IntegerField(required = False)
    d_sequence = serializers.IntegerField(required = False)
    d_name = serializers.CharField(required = False, max_length = 50)
    d_date = serializers.DateField(required = False, format="%Y-%m")
    d_status = serializers.IntegerField(required = False)
    d_place = serializers.CharField(required = False, max_length = 50)
    d_others = serializers.CharField(required = False, max_length = 200)


class RecordsViewSerializer(serializers.ModelSerializer):
    '''数据库记录视图序列化'''
    class Meta:
        model = Borrow_return_view
        fields = "__all__"


class RecordsMyViewSerializer(serializers.ModelSerializer):
    '''数据库个人记录视图序列化'''
    class Meta:
        model = Borrow_return_MyView
        fields = "__all__"