from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChiTietHopDong,HopDong,BoNhiem,NhanVienCu,TinTuyenDung
from quanlinhanvien.models import NhanVien
from ungdung.models import ChucVu
from .serializers import GetNhanVienSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count
import datetime
# Create your views here.
class qltuyendungindex(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return HttpResponse('Đây là trang quản lý tuyển dụng')

class qlhopdongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        chitiethd = ChiTietHopDong.objects.all()
        context = {'cthd' : chitiethd}
        return render(request,'qlhopdong.html',context)
class qlnghiviecView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return render(request,'quanlinghiviec.html')
    def post(self,request):
        str = ''
        id_nv = request.POST.get('maNhanVien')
        if id_nv =='':
            str = 'Hãy chọn Nhân Viên'
            context = {
                'mess': str
            }
            return render(request, 'quanlinghiviec.html', context=context)
        else :
            nhanvien = NhanVien.objects.get(id= id_nv)
        ly_do = request.POST.get('lyDo')
        y_kien = request.POST.get('ykcn')

        f_name = nhanvien.first_name
        l_name = nhanvien.last_name
        name = f_name+' '+l_name
        phone = nhanvien.phone_number
        tenchucvu = nhanvien.chuc_vu.ten_cv
        diachi = nhanvien.address
        NhanVienCu.objects.create(tennhanvien=name,tenchucvu=tenchucvu,sodienthoai = phone,diachi = diachi,
                                  lydothoiviec=ly_do,ykiencanhan = y_kien)
        nhanvien.delete()
        str = 'Đã Lưu'

        context = {
            'mess' : str
        }

        return render(request,'quanlinghiviec.html',context=context)

class qlbonhiemView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        nv = NhanVien.objects.all()
        cv = ChucVu.objects.all()
        context = {
            'nv':nv,
            'cv':cv
        }
        return render(request,'qlbonhiem.html',context=context)
    def post(self,request):
        id_nguoibn = request.POST.get('nguoiduocbonhiem')  #Pham Khoa - 14
        id_nhanvien = request.POST.get('nhanVien')
        id_chucvu = request.POST.get('selectChucVu')
        ghichu = request.POST.get('ghiChu')
        nhanvien = NhanVien.objects.get(id=id_nhanvien)
        nguoibonhiem = NhanVien.objects.get(id=id_nguoibn)
        chucvu = ChucVu.objects.get(id=id_chucvu)
        str = ''
        if nguoibonhiem.chuc_vu.id == int(id_chucvu):
            str = 'Vui Lòng Chọn Chức Vụ Khác'
        else :
            BoNhiem.objects.create(nguoiduocbonhiem= nguoibonhiem,nvbonhiem=nhanvien,chucvumoi=chucvu,ghichu=ghichu)
            str = 'Đã bầu chọn'
        nv = NhanVien.objects.all()
        cv = ChucVu.objects.all()
        context = {
            'nv': nv,
            'cv': cv,
            'mess':str
        }
        return render(request, 'qlbonhiem.html', context=context)


class themhopdongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        hopdong = HopDong.objects.all()
        context = {'hd':hopdong}
        return render(request,'themhopdong.html',context=context)
    def post(self,request):
        str = ''
        id_nv = request.POST.get('maNhanVien')
        if id_nv =='':
            str = 'Hãy chọn Nhân Viên'
            hopdong = HopDong.objects.all()
            context = {
                'hd': hopdong,
                'mess': str
            }
            return render(request, 'themhopdong.html', context=context)
        else :
            nhanvien = NhanVien.objects.get(id= id_nv)
        id_hopdong = request.POST.get('selecthopdong')
        hopdong_input = HopDong.objects.get(id=id_hopdong)
        loai_hopdong = request.POST.get('loaiHopDong')
        ngayki_input = request.POST.get('ngayKi') #yyyy//mm/dd
        ngayki_arr =  ngayki_input.split('/')

        ngayketthuc_input = request.POST.get('ngayKetThuc') #yyyy//mm/dd
        ngayketthuc_arr = ngayketthuc_input.split('/')

        try :
            d = datetime.date(int(ngayki_arr[0]),int(ngayki_arr[1]),int(ngayki_arr[2]))  # yyyy/mm//dd
            d1 = datetime.date(int(ngayketthuc_arr[0]),int(ngayketthuc_arr[1]),int(ngayketthuc_arr[2]))
            ChiTietHopDong.objects.create(nhanvien=nhanvien, hopdong=hopdong_input, loaihopdong=loai_hopdong, ngayki=d,
                                          ngayketthuc=d1)
            str = 'Thêm hợp đồng thành công'
        except :
            str = ' sai định dạng ngày tháng'

        hopdong = HopDong.objects.all()
        context = {
            'hd': hopdong,
            'mess' : str
        }

        return render(request,'themhopdong.html',context=context)
class laynhanvien(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        tennv = request.GET['tennv']
        nhanvien = NhanVien.objects.all().filter(last_name__contains=tennv)
        my_data = GetNhanVienSerializers(nhanvien,many=True)
        return Response(data = my_data.data,status = status.HTTP_200_OK)

class laymoinhanvien(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id_nv = request.GET['id']
        nhanvien = NhanVien.objects.get(id = id_nv)
        my_data = GetNhanVienSerializers(nhanvien)
        return Response(data = my_data.data,status = status.HTTP_200_OK)

class edithopdongView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        hdct = ChiTietHopDong.objects.get(id=id)
        hopdong_all = HopDong.objects.all()
        ngayki_in= hdct.ngayki.strftime('%d-%m-%Y')
        ngayketthuc_in = hdct.ngayketthuc.strftime('%d-%m-%Y')
        context = {
            'hdct':hdct,
            'hd': hopdong_all,
            'nk':ngayki_in,
            'nkt':ngayketthuc_in
        }
        return render(request,'edit_hopdong.html',context=context)
    def post(self,request,id):
        hdct = ChiTietHopDong.objects.get(id=id)
        hopdong_all = HopDong.objects.all()
        id_hopdong = request.POST.get('tenhopdong')
        hopdong = HopDong.objects.get(id = id_hopdong)
        loai_hopdong = request.POST.get('loaiHopDong')
        ngayki_input = request.POST.get('ngayKi')  # dd/mm/yyyy
        ngayki_split = ngayki_input.split('-')
        ngayketthuc_input = request.POST.get('ngayKetThuc')  # dd/mm/yyyy
        ngayketthuc_split = ngayketthuc_input.split('-')

        ngayki_in = hdct.ngayki.strftime('%d-%m-%Y')
        ngayketthuc_in = hdct.ngayketthuc.strftime('%d-%m-%Y')

        str = ''
        if loai_hopdong=='' or ngayki_input =='' or ngayketthuc_input =='':
            str = 'Vui lòng nhập đủ các trường thông tin'
            context = {
                'mess': str,
                'hdct': hdct,
                'hd': hopdong_all,
                'nk' :ngayki_in,
                'nkt':ngayketthuc_in
            }
            return render(request, 'edit_hopdong.html', context=context)
        # edit :
        try :
            d = datetime.date(int(ngayki_split[2]), int(ngayki_split[1]),int(ngayki_split[0]))  # yyyy/mm//dd
            d1 = datetime.date(int(ngayketthuc_split[2]), int(ngayketthuc_split[1]), int(ngayketthuc_split[0]))
            hdct.hopdong = hopdong
            hdct.loaihopdong = loai_hopdong
            hdct.ngayki = d
            hdct.ngayketthuc = d1
            hdct.save()
            str ='Cập Nhật Thành Công'
        except:
            str='Vui lòng nhập lại ngày'
        context = {
            'mess' : str,
            'hdct' : hdct,
            'hd' : hopdong_all
        }
        return render(request,'edit_hopdong.html',context=context)

class xoahopdong(LoginRequiredMixin,APIView):
    login_url = 'login'
    def get(self,request):
        id = request.GET['id']
        status = ''
        try:
            cthd = ChiTietHopDong.objects.get(id = id)
            cthd.delete()
            status = '200'
        except ChiTietHopDong.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")
class qlnhaviencuView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        nvcu = NhanVienCu.objects.all()
        context = {'nvc' : nvcu}
        return render(request,'chitietnhanviencu.html',context)

class chitietbonhiemView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        result = (BoNhiem.objects
                  .values('nguoiduocbonhiem')
                  .annotate(dcount=Count('nguoiduocbonhiem')))
        nv= NhanVien.objects.all()
        context = {
            'rs':result,
            'nv':nv
        }
        return render(request,'chitietbonhiem.html',context)

class chitietnguoibonhiemView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        nguoi1 = NhanVien.objects.get(id=id)
        nvbn = BoNhiem.objects.all().filter(nguoiduocbonhiem=nguoi1)
        context ={
            'nvbn': nvbn,
            'nv1':nguoi1
        }
        return render(request,'chitietbonhiem1.html',context)
class tintuyendungView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return render(request,'tintuyendung.html')
    def post(self,request):
        tieude = request.POST.get('tieuDe')
        chude = request.POST.get('chuDe')
        noidung = request.POST.get('noiDung')
        status = ''
        if tieude =='' or chude =='' or noidung=='':
            status = 'Vui lòng nhập đủ các trường thông tin'
            context = {'mess': status}
            return render(request, 'tintuyendung.html', context=context)
        try:
            TinTuyenDung.objects.create(tieude=tieude, chude=chude, noidung=noidung)
            status = 'Đăng tin thành công'
        except:
            status = 'Tiêu Đề Hoặc Chủ Đề quá dài'
        context = {'mess':status}
        return render(request,'tintuyendung.html',context=context)





