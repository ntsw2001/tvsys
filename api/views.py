#from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from app_database.models import *
# from app_utils.pagination import *
from app_utils.jwt_auth import *
from app_utils.permission import *
from django.conf import settings
import time

from django.db.models import Q
# Q对象和关键字混合使用的时候，通过关键字的查询需要写在所有的Q后面。

# Create your views here.

class Q_users(APIView):
    '''查询用户'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [Is_admin, HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data
        u_ID = data.get('u_ID')
        u_name = data.get('u_name')
        u_auth = data.get('u_auth')

        # 默认只查询普通用户
        if u_auth:
            final_u_auth = u_auth.split(',')
        else:
            final_u_auth = [1]

        if not u_name:
            u_name = ''
        if not u_ID:
            u_ID = ''

        queryset = All_users.objects.filter(u_ID__contains = u_ID,
                                            u_name__contains = u_name,
                                            u_auth__in = final_u_auth
                                            ).order_by("-u_ID")

        # pg = GlobalPagination()
        # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
        # serializer = UsersSerializer_NoPass(instance = page_queryset, many = True)
        serializer = UsersSerializer_NoPass(instance = queryset, many = True)
        return Response(serializer.data)

        # return pg.get_paginated_response(data = serializer.data)


class Q_devices(APIView):
    '''查询设备'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data
        d_ID = data.get('d_ID')
        d_name = data.get('d_name')
        d_see = data.get('d_see')
        d_type = data.get('d_type')
        #d_sequence = data.get('d_sequence')
        d_status = data.get('d_status')
        d_place = data.get('d_place')
        d_others = data.get('d_others')
        d_date_start = data.get('d_date_start')
        d_date_end = data.get('d_date_end')

        default_start_date = "1970-01-01"
        default_end_date = time.strftime('%Y-%m-%d', time.localtime())

        if d_see:
            final_d_see = d_see.split(',')
        else:
            final_d_see = [1, 9] # 默认全选

        if request.user.get_user_auth() == 1:
            final_d_see = [1]
            #return Response({"code":403, "msg":'没有权限！'})

        if d_status:
            final_d_status = d_status.split(',')
        else:
            final_d_status = [1] # 默认可借且完好的设备

        if not d_date_start:
            d_date_start = default_start_date
        if not d_date_end:
            d_date_end = default_end_date

        if not d_type:
            final_d_type = list(range(1, settings.TOTAL_TYPE + 1)) # 默认全品类
        else:
            final_d_type = d_type.split(',')

        #print(final_d_type)

        if not d_others:
            d_others = ""
        if not d_name:
            d_name = ""
        if not d_ID:
            d_ID = ""
        if not d_place:
            d_place = ""


        queryset = All_devices.objects.filter(Q(d_others__contains = d_others) | Q(d_others = None),
                                              d_see__in = final_d_see,
                                              d_type__in = final_d_type,
                                              #d_sequence = self.return_none(d_sequence),
                                              d_ID__contains = d_ID,
                                              d_name__contains = d_name,
                                              d_status__in = final_d_status,
                                              d_place__contains = d_place,
                                              d_date__range = (d_date_start, d_date_end)
                                              ).order_by("-d_ID")

        # pg = GlobalPagination()
        # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
        # serializer = DevicesSerializer(instance = page_queryset, many = True)

        # return pg.get_paginated_response(data = serializer.data)
        serializer = DevicesSerializer(instance = queryset, many = True)
        return Response(serializer.data)


class Q_records(APIView):
    '''查询记录（管理用）'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [Is_admin, HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data
        b_ID = data.get('b_ID')
        b_user = data.get('b_user')
        b_user_name = data.get('b_user_name')
        b_device = data.get('b_device')
        b_device_name = data.get('b_device_name')
        b_reason = data.get('b_reason')
        b_place = data.get('b_place')
        r_place = data.get('r_place')

        b_date_start = data.get('b_date_start')
        b_date_end = data.get('b_date_end')
        r_assign_start = data.get('r_assign_start')
        r_assign_end = data.get('r_assign_end')
        r_date_start = data.get('r_date_start')
        r_date_end = data.get('r_date_end')

        default_start_time = '1970-01-01T00:00:00'
        default_end_time = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())

        if not b_date_start:
            b_date_start = default_start_time
        if not b_date_end:
            b_date_end = default_end_time
        if not r_date_start:
            r_date_start = default_start_time
        if not r_date_end:
            r_date_end = default_end_time
        if not r_assign_start:
            r_assign_start = default_start_time
        if not r_assign_end:
            r_assign_end = default_end_time
        if not r_place:
            r_place = ''
        if not b_ID:
            b_ID = ''
        if not b_user:
            b_user = ''
        if not b_device:
            b_device = ''
        if not b_reason:
            b_reason = ''
        if not b_place:
            b_place = ''
        if not b_device_name:
            b_device_name = ''
        if not b_user_name:
            b_user_name = ''

        queryset = Borrow_return_view.objects.filter(Q(r_place__contains = r_place) | Q(r_place = None),
                                                     Q(r_assign__range = (r_assign_start, r_assign_end)) | Q(r_assign = None),
                                                     Q(r_date__range = (r_date_start, r_date_end)) | Q(r_date = None),
                                                     b_ID__contains = b_ID,
                                                     b_user__contains = b_user,
                                                     b_user_name__contains = b_user_name,
                                                     b_device__contains = b_device,
                                                     b_device_name__contains = b_device_name,
                                                     b_reason__contains = b_reason,
                                                     b_place__contains = b_place,
                                                     b_date__range = (b_date_start, b_date_end),
                                                     ).order_by("-b_date")

        # pg = GlobalPagination()
        # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
        # serializer = RecordsViewSerializer(instance = page_queryset, many = True)

        # return pg.get_paginated_response(data = serializer.data)
        serializer = RecordsViewSerializer(instance = queryset, many = True)
        return Response(serializer.data)


class Q_MyRecords(APIView):
    '''查询记录（个人用）'''

    authentication_classes = [JWTAuthentication]
    permission_classes = [HaveRefer]
    #throttle_scope = 'user'

    def post(self, request):
        data = request.data
        b_ID = data.get('b_ID')
        b_device = data.get('b_device')
        b_device_name = data.get('b_device_name')
        b_reason = data.get('b_reason')
        b_place = data.get('b_place')
        r_place = data.get('r_place')

        b_date_start = data.get('b_date_start')
        b_date_end = data.get('b_date_end')
        r_assign_start = data.get('r_assign_start')
        r_assign_end = data.get('r_assign_end')
        r_date_start = data.get('r_date_start')
        r_date_end = data.get('r_date_end')

        # 设置默认起止时间
        default_start_time = '1970-01-01T00:00:00'
        default_end_time = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())

        # 补全
        if not b_date_start:
            b_date_start = default_start_time
        if not b_date_end:
            b_date_end = default_end_time
        if not r_date_start:
            r_date_start = default_start_time
        if not r_date_end:
            r_date_end = default_end_time
        if not r_assign_start:
            r_assign_start = default_start_time
        if not r_assign_end:
            r_assign_end = default_end_time
        if not r_place:
            r_place = ''
        if not b_ID:
            b_ID = ''
        if not b_device:
            b_device = ''
        if not b_reason:
            b_reason = ''
        if not b_place:
            b_place = ''
        if not b_device_name:
            b_device_name = ''

        queryset = Borrow_return_view.objects.filter(Q(r_place__contains = r_place) | Q(r_place = None),
                                                     Q(r_assign__range = (r_assign_start, r_assign_end)) | Q(r_assign = None),
                                                     Q(r_date__range = (r_date_start, r_date_end)) | Q(r_date = None),
                                                     b_ID__contains = b_ID,
                                                     b_user = request.user.__str__(),
                                                     b_device__contains = b_device,
                                                     b_device_name__contains = b_device_name,
                                                     b_reason__contains = b_reason,
                                                     b_place__contains = b_place,
                                                     b_date__range = (b_date_start, b_date_end),
                                                     ).order_by("-b_date")

        # pg = GlobalPagination()
        # page_queryset = pg.paginate_queryset(queryset = queryset, request = request, view = self)
        # serializer = RecordsMyViewSerializer(instance = page_queryset, many = True)

        # return pg.get_paginated_response(data = serializer.data)
        serializer = RecordsMyViewSerializer(instance = queryset, many = True)
        return Response(serializer.data)