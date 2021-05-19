from django.db import models
from quanlinhanvien.models import NhanVien
# Create your models here.
class KhoaHoc(models.Model):
    tenkhoahoc = models.CharField(max_length=50,null=False)
    noidung = models.TextField(null=False)
    loaikhoahoc = models.CharField(max_length=50,default='')
    giangvien = models.CharField(max_length=50,null=True)
    mota = models.TextField(default='')
    def __str__(self):
        return self.tenkhoahoc

class ChiTietKhoaHoc(models.Model):
    ngaybatdau = models.DateField()
    ngayketthuc = models.DateField()
    soluong = 50
    khoahoc = models.ForeignKey(KhoaHoc,on_delete=models.SET_NULL,null = True,blank=True)
    nhanvien = models.ForeignKey(NhanVien,on_delete=models.CASCADE,null = True,blank=True)
    ghichu = models.TextField(default='')

    def __str__(self):
        return "Chi Tiết Khoá Học "+self.nhanvien.last_name
