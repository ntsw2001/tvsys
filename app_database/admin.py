from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(All_users)
admin.site.register(All_devices)
admin.site.register(Borrow_return)