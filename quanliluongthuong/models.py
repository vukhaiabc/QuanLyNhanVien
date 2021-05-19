from django.db import models
from quanlinhanvien.models import NhanVien
# Create your models here.
class PhuCap(models.Model):
    ten_pc = models.CharField(max_length=50,blank=True)
    loai_pc = models.CharField(max_length=50,blank=True,null=True)
    muc_pc = models.FloatField(null=False)
    def __str__(self):
        return self.ten_pc
class BacLuong(models.Model):
    ten_bl = models.CharField(max_length=50,blank=True)
    loai_bl = models.CharField(max_length=50,blank=True,null=True)
    muc_bl = models.FloatField(null=False)
    def __str__(self):
        return self.ten_bl
class Thuong(models.Model):
    ten_t = models.CharField(max_length=50,blank=True)
    loai_t = models.CharField(max_length=50,blank=True,null=True)
    muc_t = models.FloatField(null=False)
    def __str__(self):
        return self.ten_t
class LuongCoBan(models.Model):
    luong = models.FloatField()
    nhan_vien = models.ForeignKey(NhanVien,on_delete=models.CASCADE,blank=True)
    phu_cap = models.ForeignKey(PhuCap,on_delete=models.SET_NULL,null = True,blank=True)
    bac_luong = models.ForeignKey(BacLuong, on_delete=models.SET_NULL, null=True, blank=True)
    thuong = models.ForeignKey(Thuong, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nhan_vien.last_name