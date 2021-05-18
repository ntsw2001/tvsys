#from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

#router = DefaultRouter()
#router.register('users', UsersViewset, basename = 'users')

app_name = 'app_manage'

urlpatterns = [
    path('users/', UsersManageViews.as_view()),
    path('users/<str:pk>/', UsersManageViews.as_view()),
    path('devices/', DevicesManageViews.as_view()),
    path('devices/<str:pk>/', DevicesManageViews.as_view()),
    path('records/', RecordsManageViews.as_view()),
    path('records/<str:pk>/', RecordsManageViews.as_view()),
    ]# + router.urls