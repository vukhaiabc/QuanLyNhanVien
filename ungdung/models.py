from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
class ChucVu(models.Model):
    ten_cv = models.CharField(max_length=50,blank=True)
    cong_viec = models.CharField(max_length=254,blank=True)
    mo_ta = models.TextField(default='',blank=True)
    def __str__(self):
        return self.ten_cv
class PhongBan(models.Model):
    ten_pb = models.CharField(max_length=50,blank=True)
    truongphong = models.ForeignKey(User,on_delete=models.SET_NULL,null = True,blank=True)

    def __str__(self):
        return self.ten_pb
class NhanVienql(User):
    nam_kn = models.IntegerField(max_length=3,blank=True,null=True,default=0)
    phong_ban = models.ForeignKey(PhongBan,on_delete=models.SET_NULL,null = True,blank=True)
    chuc_vu =  models.ForeignKey(ChucVu,on_delete=models.SET_NULL,null = True,blank=True)
class HangSanXuat(models.Model):
    name = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class SmartPhone(models.Model):
    name = models.CharField(max_length=50,default='')
    price = models.FloatField(default=0)
    hang = models.ForeignKey(HangSanXuat,on_delete=models.SET_NULL,null = True,blank=True)

    def __str__(self):
        return self.name