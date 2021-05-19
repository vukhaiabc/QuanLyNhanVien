from django.db import models
from ungdung.models import NhanVienql
from quanlinhanvien.models import NhanVien
from ungdung.models import ChucVu
# Create your models here.
class HopDong(models.Model):
    tenhopdong = models.CharField(max_length=50,null=True)
    noidung = models.TextField(null=False)
    mota = models.TextField(default='')
    def __str__(self):
        return self.tenhopdong

class ChiTietHopDong(models.Model):
    loaihopdong = models.CharField(max_length=50, null=True)
    ngayki = models.DateField()
    ngayketthuc = models.DateField()
    hopdong = models.ForeignKey(HopDong,on_delete=models.SET_NULL,null = True,blank=True)
    nhanvien = models.ForeignKey(NhanVien,on_delete=models.SET_NULL,null = True,blank=True)
    quanli = models.ForeignKey(NhanVienql,on_delete=models.SET_NULL,null = True,blank=True)

    def __str__(self):
        return "Chi Tiet Hop Dong "+self.nhanvien.last_name
class BoNhiem(models.Model):
    nguoiduocbonhiem = models.ForeignKey(NhanVien,on_delete=models.CASCADE,null = False,related_name='nguoiduocbn')
    nvbonhiem = models.ForeignKey(NhanVien,on_delete=models.CASCADE,null = False,related_name='nhanvien')
    thoigian = models.DateTimeField(auto_now_add=True)
    chucvumoi = models.ForeignKey(ChucVu,on_delete=models.SET_NULL,null = True,blank=True)
    ghichu = models.TextField(default='')
class NhanVienCu(models.Model):
    tennhanvien = models.CharField(max_length=50)
    tenchucvu = models.CharField(max_length=50)
    sodienthoai = models.CharField(max_length=50)
    diachi = models.CharField(max_length=254)
    thoigiannghi = models.DateTimeField(auto_now_add=True,null=True)
    lydothoiviec = models.TextField(default='')
    ykiencanhan = models.TextField(default='')
class TinTuyenDung(models.Model):
    tieude = models.CharField(max_length=255)
    thoigian = models.DateTimeField(auto_now_add=True)
    chude = models.CharField(max_length=255)
    noidung = models.TextField(default='')

