from django.db import models
from django.contrib.auth.models import AbstractUser
from ungdung.models import User,ChucVu,PhongBan
# Create your models here.
class NhanVien(User):
    phong_ban = models.ForeignKey(PhongBan,on_delete=models.SET_NULL,null = True,blank=True)
    chuc_vu = models.ForeignKey(ChucVu,on_delete=models.SET_NULL,null = True,blank=True)

    def __str__(self):
        return self.last_name