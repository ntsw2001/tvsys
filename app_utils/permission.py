from rest_framework import permissions
from django.conf import settings
from app_database.models import All_users

class HaveRefer(permissions.BasePermission):
    '''判断爬虫'''
    def has_permission(self, request, view):
        if request.META.get("HTTP_REFERER"):
            return True
        return False


class Is_admin(permissions.BasePermission):
    '''判断管理员权限'''
    def has_permission(self, request, view):
        # 管理员数字符号
        admin_flag = 6

        user_auth = All_users.objects.get(pk = request.user).get_user_auth()
        if user_auth == admin_flag:
            return True
        return False