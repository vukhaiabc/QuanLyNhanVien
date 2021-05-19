from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import KhoaHoc,ChiTietKhoaHoc
from quanlinhanvien.models import NhanVien
import datetime
from django.http import HttpResponse
# Create your views here.
class qldaotaoView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        kh = KhoaHoc.objects.all()
        context = {'kh':kh}
        return render(request,'qldaotao.html',context)
class chitietmotkhoahoc(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        kh = KhoaHoc.objects.get(id = id)
        ctkh = ChiTietKhoaHoc.objects.all().filter(khoahoc = kh)
        context = {
            'ctkh':ctkh,
            'kh':kh
        }
        return render(request,'chitietkhoahoc.html',context=context)

class themkhoahoc(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        tenkh = request.GET['tenkh']
        loaikh = request.GET['loaikh']
        gvkh = request.GET['gvkh']
        noidungkh = request.GET['noidungkh']
        motakh = request.GET['motakh']
        status = ''
        if tenkh =='' or loaikh =='' or gvkh =='' or noidungkh=='' or motakh=='':
            status = '500'
        else :
            KhoaHoc.objects.create(tenkhoahoc=tenkh,loaikhoahoc = loaikh,noidung = noidungkh,giangvien=gvkh,mota = motakh)
            status = '200'
        return HttpResponse(status, content_type="application/json")
class addkhnhanvien(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        kh = KhoaHoc.objects.all()
        context = {
            'kh':kh
        }
        return render(request,'addkhoahocnhanvien.html',context=context)
    def post(self,request):
        str = ''
        id_nv = request.POST.get('maNhanVien')
        kh = KhoaHoc.objects.all()
        if id_nv =='':
            str = 'Hãy chọn Nhân Viên'
            context = {
                'kh': kh,
                'mess': str
            }
            return render(request, 'addkhoahocnhanvien.html', context=context)
        else :
            nhanvien = NhanVien.objects.get(id= id_nv)
        id_khoahoc = request.POST.get('selectKhoaHoc')
        khoahoc_input = KhoaHoc.objects.get(id=id_khoahoc)
        ngaybatdau_input = request.POST.get('ngayBatDau') #dd/mm/yyyy
        ngaybatdau_arr =  ngaybatdau_input.split('/')

        ngayketthuc_input = request.POST.get('ngayKetThuc') #dd/mm/yyyy
        ngayketthuc_arr = ngayketthuc_input.split('/')
        ghichu_input = request.POST.get('ghiChu')
        try :
            d = datetime.date(int(ngaybatdau_arr[2]),int(ngaybatdau_arr[1]),int(ngaybatdau_arr[0]))  # yyyy/mm//dd
            d1 = datetime.date(int(ngayketthuc_arr[2]),int(ngayketthuc_arr[1]),int(ngayketthuc_arr[0]))
            ChiTietKhoaHoc.objects.create(nhanvien=nhanvien, khoahoc=khoahoc_input, ngaybatdau=d,
                                          ngayketthuc=d1,ghichu = ghichu_input)
            str = 'Thêm khoá đào tạo thành công'
        except :
            str = ' Sai định dạng ngày tháng'

        context = {
            'kh': kh,
            'mess' : str
        }

        return render(request,'addkhoahocnhanvien.html',context=context)
