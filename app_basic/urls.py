from django.urls import path, include
from .views import *

app_name = 'app_basic'

urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('lend/', Lend.as_view(), name = 'lend'),
    path('reset/', ResetPass.as_view(), name = 'reset'),
    path('modify/', ModifyPass.as_view(), name = 'modify'),
    path('return/', Retun.as_view(), name = 'return'),
    path('return/<str:pk>/', Retun.as_view(), name = 'return'),
    ]
