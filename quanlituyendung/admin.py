from django.contrib import admin
from .models import HopDong,ChiTietHopDong,BoNhiem,NhanVienCu,TinTuyenDung
# Register your models here.
admin.site.register(HopDong)
admin.site.register(ChiTietHopDong)
admin.site.register(BoNhiem)
admin.site.register(TinTuyenDung)
admin.site.register(NhanVienCu)