from rest_framework import serializers
from .models import PhuCap,Thuong,BacLuong,LuongCoBan
# serialize : chuyen du lieu sang client (trung gian)
class GetPhuCapSerializers(serializers.ModelSerializer):
    class Meta :
        model = PhuCap
        fields =['id','ten_pc','loai_pc','muc_pc']
class GetBacLuongSerializers(serializers.ModelSerializer):
    class Meta :
        model = BacLuong
        fields =['id','ten_bl','loai_bl','muc_bl']

class GetThuongSerializers(serializers.ModelSerializer):
    class Meta :
        model = Thuong
        fields =['id','ten_t','loai_t','muc_t']

class PostProductSerializers(serializers.Serializer):
    name1 = serializers.CharField(max_length=50)
    price1 = serializers.FloatField(default=0)
    type1 = serializers.CharField(max_length=50)
    desc1 = serializers.CharField(max_length=50)
