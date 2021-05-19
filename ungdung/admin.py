from django.contrib import admin
from .models import User,HangSanXuat,SmartPhone,NhanVienql,ChucVu,PhongBan
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User)
admin.site.register(NhanVienql)
admin.site.register(ChucVu)
admin.site.register(PhongBan)
admin.site.register(HangSanXuat)
admin.site.register(SmartPhone)

