from django.urls import path, include
from .views import *

app_name = 'api'

urlpatterns = [
    path('q_u/', Q_users.as_view(), name = 'qu'),
    path('q_d/', Q_devices.as_view(), name = 'qd'),
    path('q_r/', Q_records.as_view(), name = 'qr'),
    path('q_mr/', Q_MyRecords.as_view(), name = 'qmr'),
    ]