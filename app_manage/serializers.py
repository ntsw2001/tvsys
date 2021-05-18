from rest_framework import serializers
from app_database.models import *
import hashlib
from datetime import datetime
from django.db.models import Max

# Serializer 的构造函数的参数，如下：
# 1. instance: 传递一个ORM对象或queryset对象，将该对象序列化为JSON
# 2. data: 传递一个需要验证是否符合要求的数据
# 3. many: 当且仅当instance是一个queryset对象，则添加该参数并 =True

class UsersSerializer(serializers.Serializer):
    '''用户序列化'''
    u_ID = serializers.CharField(max_length = 15, required = False,
                                 error_messages = {"required":"学号或工号不能为空！", "max_length":"长度不能大于15！"})
    u_name = serializers.CharField(max_length = 15, required = False,
                                   error_messages = {"required":"姓名不能为空！", "max_length":"长度不能大于15！"})
    u_pass = serializers.CharField(max_length = 256, required = False,
                                   error_messages = {"required":"请设置默认密码或自定义密码！"})
    u_auth = serializers.IntegerField(required = False,
                                      error_messages = {"required":"请设置权限！"})

    def update(self, instance, validated_data):
        '''重写修改'''
        instance.u_ID = validated_data.get('u_ID', instance.u_ID)
        instance.u_name = validated_data.get('u_name', instance.u_name)
        instance.u_auth = validated_data.get('u_auth', instance.u_auth)

        # 密码加密处理
        temp = validated_data.get('u_pass')
        if not temp:
            instance.u_pass = validated_data.get(temp, instance.u_pass)# 第一个temp实参必须要有
        else:
            pwd = hashlib.sha256(temp.encode('utf-8')).hexdigest()
            instance.u_pass = pwd

        instance.save()
        return instance

    def create(self, validated_data):
        '''重写创建'''
        uid = validated_data.get('u_ID')
        uname = validated_data.get('u_name')
        uauth = validated_data.get('u_auth')
        pwd = hashlib.sha256(validated_data.get('u_pass').encode('utf-8')).hexdigest()

        return All_users.objects.create(u_ID = uid, u_name = uname, u_pass = pwd, u_auth = uauth)


class DevicesSerializer(serializers.Serializer):
    '''设备序列化'''
    d_ID = serializers.CharField(required = False, max_length = 12,
                                 error_messages = {"required":"设备ID不能为空！", "max_length":"长度不能大于12！"})
    d_see = serializers.IntegerField(required = False,
                                     error_messages = {"required":"设备可见等级不能为空！"})
    d_type = serializers.IntegerField(required = False,
                                      error_messages = {"required":"设备类型不能为空！"})
    d_sequence = serializers.IntegerField(required = False,
                                         error_messages = {"required":"设备序列不能为空！"})
    d_name = serializers.CharField(required = False, max_length = 50,
                                   error_messages = {"required":"设备名不能为空！", "max_length":"长度不能大于15！"})
    d_date = serializers.DateField(required = False, format="%Y-%m-%d",
                                   error_messages = {"required":"设备使用日期不能为空！"})
    d_status = serializers.IntegerField(required = False,
                                        error_messages = {"required":"设备状态不能为空！"})
    d_place = serializers.CharField(required = False, max_length = 50,
                                    error_messages = {"required":"设备所在地不能为空！", "max_length":"长度不能大于50！"})
    d_others = serializers.CharField(required = False, max_length = 200, allow_null = True,
                                     error_messages = {"max_length":"长度不能大于200！"})

    def update(self, instance, validated_data):
        '''重写修改'''
        instance.d_ID = validated_data.get(None, instance.d_ID)# 设备严禁变更ID
        instance.d_see = validated_data.get('d_see', instance.d_see)
        instance.d_type = validated_data.get(None, instance.d_type)# 严禁变更类别
        instance.d_sequence = validated_data.get(None, instance.d_sequence)# 严禁变更序列
        instance.d_date = validated_data.get('d_date', instance.d_date)
        instance.d_name = validated_data.get('d_name', instance.d_name)
        instance.d_status = validated_data.get('d_status', instance.d_status)
        instance.d_place = validated_data.get('d_place', instance.d_place)
        instance.d_others = validated_data.get('d_others', instance.d_others)

        instance.save()
        return instance

    def create(self, validated_data):
        '''重写创建'''
        dsee = validated_data.get('d_see')
        dtype = validated_data.get('d_type')
        dname = validated_data.get('d_name')
        ddate = validated_data.get('d_date')
        dstatus = validated_data.get('d_status')
        dplace = validated_data.get('d_place')
        dothers = validated_data.get('d_others')

        # sequence
        if All_devices.objects.filter(d_type = dtype):
            #from django.db.models import Max
            dsequence = 1 + All_devices.objects.filter(d_type = dtype).aggregate(Max('d_sequence'))['d_sequence__max']
        else:
            dsequence = 1

        # ID
        did = ddate.strftime("%Y%m") + str(dtype).zfill(3) + str(dsequence).zfill(3)

        return All_devices.objects.create(d_ID = did, d_see = dsee, d_type = dtype, 
                                        d_sequence = dsequence, d_name = dname, d_date = ddate,
                                        d_status = dstatus, d_place = dplace, d_others = dothers)


class RecordsSerializer(serializers.Serializer):
    '''记录序列化'''
    b_ID = serializers.CharField(required = False, max_length = 20,
                                 error_messages = {"required":"记录ID不能为空！", "max_length":"长度不能大于20！"})
    b_user = serializers.CharField(required = False, max_length = 15,
                                   error_messages = {"required":"借用人ID不能为空！", "max_length":"长度不能大于15！"})
    b_device = serializers.CharField(required = False, max_length = 12,
                                     error_messages = {"required":"被借设备ID不能为空！", "max_length":"长度不能大于12！"})
    b_date = serializers.DateTimeField(required = False, format='%Y-%m-%d %H:%M:%S',
                                       error_messages = {"required":"借用日期不能为空！"})
    b_reason = serializers.CharField(required = False, max_length = 100,
                                     error_messages = {"required":"借用理由不能为空！", "max_length":"长度不能大于100！"})
    b_place = serializers.CharField(required = False, max_length = 50,
                                    error_messages = {"required":"设备所在地不能为空！", "max_length":"长度不能大于50！"})
    r_assign = serializers.DateTimeField(required = False, format='%Y-%m-%d %H:%M:%S', allow_null = True)
    r_date = serializers.DateTimeField(required = False, format='%Y-%m-%d %H:%M:%S', allow_null = True,
                                       error_messages = {"required":"实际归还时间不能为空！"})
    r_place = serializers.CharField(required = False, max_length = 50, allow_null = True,
                                    error_messages = {"required":"设备归还地不能为空！", "max_length":"长度不能大于50！"})

    def update(self, instance, validated_data):
        '''重写修改'''
        instance.b_ID = validated_data.get(None, instance.b_ID)# 记录严禁变更ID

        if validated_data.get('b_user'):
            instance.b_user = All_users.objects.get(u_ID = validated_data.get('b_user'))
        else:
            instance.b_user = validated_data.get(None, instance.b_user)

        if validated_data.get('b_device'):
            instance.b_device = All_devices.objects.get(b_ID = validated_data.get('b_device'))
        else:
            instance.b_device = validated_data.get(None, instance.b_device)

        instance.b_date = validated_data.get('b_date', instance.b_date)
        instance.b_reason = validated_data.get('b_reason', instance.b_reason)
        instance.b_place = validated_data.get('b_place', instance.b_place)
        instance.r_assign = validated_data.get('r_assign', instance.r_assign)
        instance.r_date = validated_data.get('r_date', instance.r_date)
        instance.r_place = validated_data.get('r_place', instance.r_place)

        instance.save()
        return instance

    def create(self, validated_data):
        '''重写创建'''
        buser = All_users.objects.get(u_ID = validated_data.get('b_user'))
        bdevice = All_devices.objects.get(d_ID = validated_data.get('b_device'))
        bdate = validated_data.get('b_date')
        breason = validated_data.get('b_reason')
        bplace = validated_data.get('b_place')
        rassign = validated_data.get('r_assign')
        rdate = validated_data.get('r_date')
        rplace = validated_data.get('r_place')

        # 第几次
        query_date_start = bdate.strftime("%Y-%m-%d") + "T00:00:00"
        query_date_end = bdate.strftime("%Y-%m-%d") + "T23:59:00"
        if Borrow_return.objects.filter(b_user = buser, b_date__range = (query_date_start, query_date_end)):
            #from django.db.models import Count
            bsequence = 1 + Borrow_return.objects.filter(b_user = buser, b_date__range = (query_date_start, query_date_end)).count()
        else:
            bsequence = 1

        # ID
        bid = buser.__str__() + bdate.strftime("%Y%m%d") + str(bsequence).zfill(3)

        return Borrow_return.objects.create(b_ID = bid, b_user = buser, b_device = bdevice, 
                                        b_date = bdate, b_reason = breason, b_place = bplace,
                                        r_assign = rassign, r_date = rdate, r_place = rplace)


class UsersSerializer_NoPass(serializers.ModelSerializer):
    '''不返回密码的用户序列化'''
    class Meta:
        model = All_users
        exclude = ['u_pass']


class RecordsViewSerializer(serializers.ModelSerializer):
    '''数据库记录视图序列化'''
    class Meta:
        model = Borrow_return_view
        fields = "__all__"