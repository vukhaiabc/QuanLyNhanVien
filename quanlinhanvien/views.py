from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import NhanVien
from django.http import HttpResponse
from ungdung.models import ChucVu,PhongBan,User
import re
# Create your views here.
class index_qlnhanvien(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        nhanvien_all =NhanVien.objects.all()
        context ={'nhanvien' : nhanvien_all}
        return render(request,'qlnhanvien.html',context=context)
class profileView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        nhanvien_index = NhanVien.objects.get(id = id)
        context = {'us':nhanvien_index}
        return render(request,'profile_nhanvien.html',context=context)
class addnhanvienView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        chucvu_all = ChucVu.objects.all()
        phongban_all = PhongBan.objects.all()
        context = {
            'cv':chucvu_all,
            'pb':phongban_all
        }
        return render(request,'add_nhanvien.html',context=context)
    def post(self,request):
        username = request.POST.get('tendangnhap')
        email = request.POST.get('email')
        password = request.POST.get('matkhau')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        id_phongban = request.POST.get('phongban')
        phong_ban = PhongBan.objects.get(id = id_phongban)
        id_chucvu = request.POST.get('chucvu')
        chuc_vu = ChucVu.objects.get(id=id_chucvu)
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        str = ''
        Flag = False
        if re.search(r'^\w+$', username):
            try:
                User.objects.get(username=username)
                str = 'User đã tồn tại, Vui lòng chon tên đăng nhập khác!'
            except User.DoesNotExist:
                NhanVien.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    chuc_vu= chuc_vu,
                    phong_ban= phong_ban,
                    phone_number = phone,
                    address = address
                )
                str = 'Bạn đã đăng kí thành công!'
                Flag = True
        else:
            str = 'User chứa kí tự đặc biệt !!!'
        chucvu_all = ChucVu.objects.all()
        phongban_all = PhongBan.objects.all()
        context = {
            'flag':Flag,
            'mess': str,
            'cv': chucvu_all,
            'pb': phongban_all
        }
        return render(request, 'add_nhanvien.html', context=context)

class editnhanvienView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,id):
        nhanvien_index = NhanVien.objects.get(id=id)
        chucvu_all = ChucVu.objects.all()
        phongban_all = PhongBan.objects.all()
        context = {
            'us':nhanvien_index,
            'cv': chucvu_all,
            'pb': phongban_all
        }
        return render(request,'edit_nhanvien.html',context=context)
    def post(self,request,id):
        email = request.POST.get('email')
        password = request.POST.get('matkhau')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        id_phongban = request.POST.get('phongban')
        phong_ban = PhongBan.objects.get(id = id_phongban)
        id_chucvu = request.POST.get('chucvu')
        chuc_vu = ChucVu.objects.get(id=id_chucvu)
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        flag = True
        nhanvien_edit = NhanVien.objects.get(id=id)
        if email=='' or password=='' or first_name=='' or last_name=='' or phone=='' or address=='':
            flag = False
            str ='Phải điền đầy đủ vào các ô trống!!!'
        if flag:
            nhanvien_edit.email = email
            nhanvien_edit.first_name = first_name
            nhanvien_edit.last_name = last_name
            nhanvien_edit.phone_number = phone
            nhanvien_edit.address = address
            nhanvien_edit.chuc_vu = chuc_vu
            nhanvien_edit.phong_ban = phong_ban
            nhanvien_edit.set_password(password)
            nhanvien_edit.save()
            str = 'Đã Lưu'
        chucvu_all = ChucVu.objects.all()
        phongban_all = PhongBan.objects.all()
        context = {
            'us':nhanvien_edit,
            'mess': str,
            'cv': chucvu_all,
            'pb': phongban_all,
            'flag' : flag
        }
        return render(request, 'edit_nhanvien.html', context=context)
class xoanhanvien(LoginRequiredMixin,View):
    login_url = 'login'

    def get(self, request):
        id = request.GET['id']
        status = ''
        try:
            nv = NhanVien.objects.get(id=id)
            nv.delete()
            status = '200'
        except NhanVien.DoesNotExist:
            status = '500'
        return HttpResponse(status, content_type="application/json")