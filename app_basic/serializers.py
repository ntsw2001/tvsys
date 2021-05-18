from rest_framework import serializers
from app_database.models import *
from datetime import datetime
from django.db.models import Max

class RecordsSerializer(serializers.Serializer):
    '''记录序列化 该版本特化自app_manage'''
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
        instance.b_ID = validated_data.get(None, instance.b_ID)
        instance.b_user = validated_data.get(None, instance.b_user)
        instance.b_device = validated_data.get(None, instance.b_device)
        instance.b_date = validated_data.get(None, instance.b_date)
        instance.b_reason = validated_data.get(None, instance.b_reason)
        instance.b_place = validated_data.get(None, instance.b_place)
        instance.r_assign = validated_data.get(None, instance.r_assign)
        instance.r_date = validated_data.get('r_date')
        instance.r_place = validated_data.get('r_place')

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

        # 今日第几次
        query_date_start = bdate.strftime("%Y-%m-%d") + "T00:00:00"
        query_date_end = bdate.strftime("%Y-%m-%d") + "T23:59:00"
        if Borrow_return.objects.filter(b_user = buser, b_date__range = (query_date_start, query_date_end)):
            #from django.db.models import Count
            temp = Borrow_return.objects.filter(b_user = buser, b_date__range = (query_date_start, query_date_end)).aggregate(Max('b_ID'))['b_ID__max'][-3:]
            bsequence = 1 + int(temp)
        else:
            bsequence = 1

        # ID
        bid = buser.__str__() + bdate.strftime("%Y%m%d") + str(bsequence).zfill(3)

        return Borrow_return.objects.create(b_ID = bid, b_user = buser, b_device = bdevice, 
                                        b_date = bdate, b_reason = breason, b_place = bplace,
                                        r_assign = rassign, r_date = rdate, r_place = rplace)


class RecordsMyViewSerializer(serializers.ModelSerializer):
    '''数据库个人记录视图序列化'''
    class Meta:
        model = Borrow_return_MyView
        fields = "__all__"