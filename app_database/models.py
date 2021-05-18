from django.db import models
import hashlib

# Create your models here.

# 用户表
class All_users(models.Model):
    '''用户表'''
    u_ID = models.CharField(db_column = 'u_ID', primary_key = True, null = False, max_length = 15, unique = True)
    u_name = models.CharField(db_column = 'u_name', null = False, max_length = 15)
    u_pass = models.CharField(db_column = 'u_pass', null = False, max_length = 256)
    u_auth = models.IntegerField(db_column = 'u_auth', null = False, default = 1)

    class Meta:
        managed = True
        db_table = 'users'# 设置迁移后表的名字'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.u_ID

    def __str__(self):
        return self.u_ID

    def get_user_name(self):
        return self.u_name

    def get_user_auth(self):
        return self.u_auth

    def set_pass(self, u_pass):
        self.u_pass = u_pass
        self.save()

    """
    def save(self, *args, **kwargs):
        '''自定义 save 方法'''
        self.u_pass = hashlib.sha256(self.u_pass.encode('utf-8')).hexdigest()
    """
    

# 设备表
class All_devices(models.Model):
    '''设备表'''
    d_ID = models.CharField(db_column = 'd_ID', primary_key = True, null = False, max_length = 12, unique = True)
    d_see = models.IntegerField(db_column = 'd_see', null = False, default = 1)
    d_type = models.IntegerField(db_column = 'd_type', null = False)
    d_sequence = models.IntegerField(db_column = 'd_sequence', null = False)
    d_name = models.CharField(db_column = 'd_name', null = False, max_length = 50)
    d_date = models.DateField(db_column = 'd_date', null = False)
    d_status = models.IntegerField(db_column = 'd_status', null = False, default = 1)
    d_place = models.CharField(db_column = 'd_place', null = False, max_length = 50)
    d_others = models.CharField(db_column = 'd_others', null = True, max_length = 200)

    class Meta:
        managed = True
        db_table = 'devices'
        verbose_name_plural = 'devices'

    def __unicode__(self):
        return self.d_ID

    def __str__(self):
        return self.d_ID

    def get_device_name(self):
        return self.d_name

    def get_device_place(self):
        return self.d_place

    def get_device_status(self):
        return self.d_status

    def set_status(self, status):
        self.d_status = status
        self.save()

    def set_place(self, place):
        self.d_place = place
        self.save()


# 借还记录
class Borrow_return(models.Model):
    '''记录表'''
    b_ID = models.CharField(db_column = 'b_ID', primary_key = True, null = False, max_length = 30, unique = True)
    #b_user = models.CharField(db_column = 'b_user', null = True, max_length = 15)
    b_user = models.ForeignKey(All_users, on_delete = models.CASCADE, db_column = 'b_user')
    #b_device = models.CharField(db_column = 'b_device', null = True, max_length = 12)
    b_device = models.ForeignKey(All_devices, on_delete = models.CASCADE, db_column = 'b_device')
    b_date = models.DateTimeField(db_column = 'b_date', null = False)
    b_reason = models.CharField(db_column = 'b_reason', null = False, max_length = 100)
    b_place = models.CharField(db_column = 'b_place', null = False, max_length = 50)
    r_assign = models.DateTimeField(db_column = 'r_assign', null = True)
    r_date = models.DateTimeField(db_column = 'r_date', null = True)
    r_place = models.CharField(db_column = 'r_place', null = True, max_length = 50)
    
    class Meta:
        managed = True
        db_table = 'borrow_return'
        verbose_name_plural = 'borrow_return'

    def __unicode__(self):
        return self.b_ID

    def __str__(self):
        return self.b_ID

    def get_device(self):
        return self.b_device


# 借还记录的数据库视图
class Borrow_return_view(models.Model):
    '''借还记录的数据库视图'''
    b_ID = models.CharField(db_column = 'b_ID', primary_key = True, null = False, max_length = 30, unique = True)
    b_user = models.CharField(db_column = 'b_user', max_length = 15, null = False)
    b_user_name = models.CharField(db_column = 'b_user_name', null = False, max_length = 15)
    b_device = models.CharField(db_column = 'b_device', max_length = 12, null = False)
    b_device_name = models.CharField(db_column = 'b_device_name', null = False, max_length = 50)
    b_date = models.DateTimeField(db_column = 'b_date', null = False)
    b_reason = models.CharField(db_column = 'b_reason', null = False, max_length = 100)
    b_place = models.CharField(db_column = 'b_place', null = False, max_length = 50)
    r_assign = models.DateTimeField(db_column = 'r_assign', null = True)
    r_date = models.DateTimeField(db_column = 'r_date', null = True)
    r_place = models.CharField(db_column = 'r_place', null = True, max_length = 50)

    class Meta:
        managed = False # 不迁移该表
        db_table = "view_records"


# 借还记录创建者自查视图
class Borrow_return_MyView(models.Model):
    '''借还记录创建者自查视图'''
    b_ID = models.CharField(db_column = 'b_ID', primary_key = True, null = False, max_length = 30, unique = True)
    b_user = models.CharField(db_column = 'b_user', max_length = 15, null = False)
    b_device = models.CharField(db_column = 'b_device', max_length = 12, null = False)
    b_device_name = models.CharField(db_column = 'b_device_name', null = False, max_length = 50)
    b_date = models.DateTimeField(db_column = 'b_date', null = False)
    b_reason = models.CharField(db_column = 'b_reason', null = False, max_length = 100)
    b_place = models.CharField(db_column = 'b_place', null = False, max_length = 50)
    r_assign = models.DateTimeField(db_column = 'r_assign', null = True)
    r_date = models.DateTimeField(db_column = 'r_date', null = True)
    r_place = models.CharField(db_column = 'r_place', null = True, max_length = 50)

    class Meta:
        managed = False # 不迁移该表
        db_table = "view_myrecords"