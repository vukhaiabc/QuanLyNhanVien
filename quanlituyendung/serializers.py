from rest_framework import serializers
from quanlinhanvien.models import NhanVien
# serialize : chuyen du lieu sang client (trung gian)
class GetNhanVienSerializers(serializers.ModelSerializer):
    class Meta :
        model = NhanVien
        fields =['id','username','first_name','last_name','phong_ban','chuc_vu','phone_number','email','address']




