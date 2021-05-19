from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PhuCap,Thuong,BacLuong,LuongCoBan
from quanlinhanvien.models import NhanVien
from .serializers import GetPhuCapSerializers,GetBacLuongSerializers,GetThuongSerializers
# Create your views here.
class qlluongthuongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return HttpResponse("Trang QL luong thuong")

class qlluongnhanvienView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        luong_all = LuongCoBan.objects.all()
        context = {'lnv' : luong_all}
        return render(request,'qlluongnhanvien.html',context=context)



class qlbacluongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        bacluong_all = BacLuong.objects.all()
        context = {'bl' : bacluong_all}
        return render(request,'qlbacluong.html',context=context)
    def post(self,request):
        pass

class qlphucapView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        phucap_all = PhuCap.objects.all()
        context = {'pc' : phucap_all}
        return render(request,'qlphucap.html',context=context)
    def post(self,request):
        ten_pc = request.POST.get('tenpc')
        loai_pc = request.POST.get('loaipc')
        muc_pc = request.POST.get('mucpc')
        str =''
        try :
            PhuCap.objects.get(ten_pc=ten_pc)
            str = 'Phụ Cấp đã tồn tại'
        except PhuCap.DoesNotExist:
            PhuCap.objects.create(ten_pc=ten_pc,loai_pc=loai_pc,muc_pc=muc_pc)
            str = ' Thành công'
        phucap_all = PhuCap.objects.all()
        context = {
            'mess':str,
            'pc':phucap_all
        }
        return render(request, 'qlphucap.html', context=context)
class qlthuongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        thuong_all = Thuong.objects.all()
        context = {'thuong' : thuong_all}
        return render(request,'qlthuong.html',context=context)

class themluongnhanvienView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        phucap_all = PhuCap.objects.all()
        thuong_all = Thuong.objects.all()
        bacluong_all = BacLuong.objects.all()
        context = {
            'pc':phucap_all,
            'thuong':thuong_all,
            'bl':bacluong_all
        }
        return render(request,'addluongnhanvien.html',context=context)
    def post(self,request):
        id_nv = request.POST.get('maNhanVien')
        bacluong_in = request.POST.get('selectbacluong')
        phucap_in = request.POST.get('selectphucap')
        thuong_in = request.POST.get('selectthuong')
        str=''
        if id_nv == '':
            str='Hãy Chọn Nhân Viên'
        else :
            nhanvien = NhanVien.objects.get(id = id_nv)
            try:
                LuongCoBan.objects.get(nhan_vien = nhanvien)
                str = 'Nhân Viên đã tồn tại trong hệ thống'

            except LuongCoBan.DoesNotExist:
                bool_bacluong = False
                bool_phucap = False
                bool_thuong = False
                bacluong_select = None
                phucap_select = None
                thuong_select = None
                if bacluong_in != '':
                    bacluong_select = BacLuong.objects.get(id=bacluong_in)
                    bool_bacluong=True
                if phucap_in != '':
                    phucap_select = PhuCap.objects.get(id=phucap_in)
                    bool_phucap=True
                if thuong_in !='':
                    thuong_select = Thuong.objects.get(id=thuong_in)
                    bool_thuong = True
                total_luong = 0
                if bool_bacluong:
                    total_luong += bacluong_select.muc_bl
                if bool_phucap:
                    total_luong += phucap_select.muc_pc
                if bool_thuong:
                    total_luong += thuong_select.muc_t

                LuongCoBan.objects.create(luong = total_luong,nhan_vien = nhanvien,bac_luong=bacluong_select,
                                          phu_cap = phucap_select, thuong=thuong_select)
                str = 'Thêm Thành Công'

        phucap_all = PhuCap.objects.all()
        thuong_all = Thuong.objects.all()
        bacluong_all = BacLuong.objects.all()
        context = {
            'mess':str,
            'pc': phucap_all,
            'thuong': thuong_all,
            'bl': bacluong_all
        }
        return render(request, 'addluongnhanvien.html', context=context)


class luuphucap(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        tenpc = request.GET['tenpc']
        loaipc = request.GET['loaipc']
        mucpc = request.GET['mucpc']

        status = ''
        try:
            PhuCap.objects.get(ten_pc=tenpc)
            status = '500'
        except PhuCap.DoesNotExist:
            PhuCap.objects.create(ten_pc=tenpc, loai_pc=loaipc, muc_pc=mucpc)
            status = '200'
        return HttpResponse(status, content_type="application/json")
class thembacluong(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        tenbl = request.GET['tenbl']
        loaibl = request.GET['loaibl']
        mucbl = request.GET['mucbl']

        status = ''
        try:
            BacLuong.objects.get(ten_bl=tenbl)
            status = '500'
        except BacLuong.DoesNotExist:
            BacLuong.objects.create(ten_bl=tenbl, loai_bl=loaibl, muc_bl=mucbl)
            status = '200'
        return HttpResponse(status, content_type="application/json")

class themthuong(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        tent = request.GET['tent']
        loait = request.GET['loait']
        muct = request.GET['muct']

        status = ''
        try:
            Thuong.objects.get(ten_t=tent)
            status = '500'
        except Thuong.DoesNotExist:
            Thuong.objects.create(ten_t=tent, loai_t=loait, muc_t=muct)
            status = '200'
        return HttpResponse(status, content_type="application/json")

class layphucap(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        phucap = PhuCap.objects.get(id=id)
        my_data = GetPhuCapSerializers(phucap)
        return Response(data = my_data.data,status = status.HTTP_200_OK)

class laybacluong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        bacluong = BacLuong.objects.get(id=id)
        my_data = GetBacLuongSerializers(bacluong)
        return Response(data = my_data.data,status = status.HTTP_200_OK)

class laythuong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        thuong = Thuong.objects.get(id=id)
        my_data = GetThuongSerializers(thuong)
        return Response(data = my_data.data,status = status.HTTP_200_OK)

class capnhatphucap(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        tenpc = request.GET['tenpc']
        loaipc = request.GET['loaipc']
        mucpc = request.GET['mucpc']

        status = ''
        try:
            phucap_index = PhuCap.objects.get(id=id)
            phucap_index.ten_pc = tenpc
            phucap_index.loai_pc = loaipc
            phucap_index.muc_pc = mucpc
            phucap_index.save()
            status = '200'
        except PhuCap.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class capnhatbacluong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        tenbl = request.GET['tenbl']
        loaibl = request.GET['loaibl']
        mucbl = request.GET['mucbl']

        status = ''
        try:
            bacluong_index = BacLuong.objects.get(id=id)
            bacluong_index.ten_bl = tenbl
            bacluong_index.loai_bl = loaibl
            bacluong_index.muc_bl = mucbl
            bacluong_index.save()
            status = '200'
        except BacLuong.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class capnhatthuong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        tent = request.GET['tent']
        loait = request.GET['loait']
        muct = request.GET['muct']

        status = ''
        try:
            thuong_index = Thuong.objects.get(id=id)
            thuong_index.ten_t = tent
            thuong_index.loai_t = loait
            thuong_index.muc_t = muct
            thuong_index.save()
            status = '200'
        except Thuong.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class xoaphucap(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        status = ''
        try:
            phu_cap = PhuCap.objects.get(id = id)
            phu_cap.delete()
            status = '200'
        except PhuCap.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class xoabacluong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        status = ''
        try:
            bac_luong = BacLuong.objects.get(id = id)
            bac_luong.delete()
            status = '200'
        except BacLuong.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class xoathuong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        status = ''
        try:
            thuong = Thuong.objects.get(id = id)
            thuong.delete()
            status = '200'
        except Thuong.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")

class xoaluongnhanvien(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        status = ''
        try:
            lcbnv = LuongCoBan.objects.get(id = id)
            lcbnv.delete()
            status = '200'
        except LuongCoBan.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")
class editluongnhanvien(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request,id):
        luongnv = LuongCoBan.objects.get(id=id)
        phucap_all = PhuCap.objects.all()
        thuong_all = Thuong.objects.all()
        bacluong_all = BacLuong.objects.all()
        context = {
            'luongnv': luongnv,
            'pc': phucap_all,
            'thuong': thuong_all,
            'bl': bacluong_all
        }
        return render(request, 'editluongnhanvien.html', context=context)
    def post(self,request,id):
        luong_update = LuongCoBan.objects.get(id=id)
        id_bl = request.POST.get('selectbacluong')
        id_pc = request.POST.get('selectphucap')
        id_t = request.POST.get('selectthuong')

        bool_bacluong = False
        bool_phucap = False
        bool_thuong = False
        bacluong_select = None
        phucap_select = None
        thuong_select = None
        if id_bl != '':
            bacluong_select = BacLuong.objects.get(id=id_bl)
            bool_bacluong = True
        if id_pc != '':
            phucap_select = PhuCap.objects.get(id=id_pc)
            bool_phucap = True
        if id_t != '':
            thuong_select = Thuong.objects.get(id=id_t)
            bool_thuong = True
        total_luong = 0
        if bool_bacluong:
            total_luong+= bacluong_select.muc_bl
        if bool_phucap :
            total_luong+=phucap_select.muc_pc
        if bool_thuong:
            total_luong+=thuong_select.muc_t

        luong_update.bac_luong = bacluong_select
        luong_update.phu_cap = phucap_select
        luong_update.thuong = thuong_select
        luong_update.luong = total_luong
        luong_update.save()
        str ='Sửa Thành Công'
        phucap_all = PhuCap.objects.all()
        thuong_all = Thuong.objects.all()
        bacluong_all = BacLuong.objects.all()
        context = {
            'mess':str,
            'luongnv': luong_update,
            'pc': phucap_all,
            'thuong': thuong_all,
            'bl': bacluong_all
        }
        return render(request, 'editluongnhanvien.html', context=context)
