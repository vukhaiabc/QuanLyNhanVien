from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HangSanXuat,SmartPhone,User,NhanVienql
from quanlinhanvien.models import NhanVien
import re
# Create your views here.
class registermember(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        str =''
        if re.search(r'^\w+$', username):
            try:
                User.objects.get(username=username)
                str = 'User đã tồn tại, Vui lòng chon tên đăng nhập khác!'
            except User.DoesNotExist:
                if password1 !=password2:
                    str = 'mật khẩu không khớp'
                else : #tao tai khoan chi cho nhan vien quan ly
                    NhanVienql.objects.create_user(username=username,email=email,password=password1)
                    str = 'Bạn đã đăng kí thành công!'
        else : str = 'User chứa kí tự đặc biệt !!!'
        context = {'mess': str}
        return render(request, 'register.html',context=context)
class index(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        num_nhanvien = NhanVien.objects.all().count()
        num_quanli = NhanVienql.objects.all().count()
        context = {
            'num_nv':num_nhanvien,
            'num_ql': num_quanli,
        }
        return render(request,'index.html',context)
class loginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        us = request.POST.get('username')
        pw = request.POST.get('password')
        str=''
        try :
            NhanVienql.objects.get(username= us)
            user = authenticate(username=us, password=pw)
            if user:
                login(request, user)
                return redirect('index_view')
            else:
                str='Mật khẩu không đúng !'
        except NhanVienql.DoesNotExist:
            str = 'Tài khoản không tồn tại'
        context = {
            'mess':str,
        }
        return render(request,'login.html',context)
def logout_view(request):
    logout(request)
    return redirect('login')
class changepasswordView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        return render(request,'changepassword.html')
    def post(self,request):
        pw_old = request.POST.get('old')
        pw_new = request.POST.get('new1')
        pw_new1 = request.POST.get('new2')
        us = request.user
        str =''
        if pw_old =='' or pw_new =='' or pw_new1 =='':
            str = 'Mật khẩu không được để trống!'
            return render(request, 'changepassword.html', context={'mess':str})
        user_log = authenticate(username=us.username, password=pw_old)
        if user_log :
            if pw_new != pw_new1 :
                str ='Mật khẩu mới không khớp!'
            else :
                if pw_old != pw_new :
                    us.set_password(pw_new)
                    us.save()
                    user_login_new = authenticate(username=us.username, password=pw_new)
                    login(request,user_login_new)
                    str ='Thành Công!!!'
                else :
                    str ='Mật khẩu cũ và mới không được trùng nhau!'
        else : str ='Mật khẩu hiện tại sai, Vui lòng nhập lại!'
        context = {'mess':str}
        return render(request,'changepassword.html',context=context)
class profileView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        us = request.user
        context = {'us':us}
        return render(request,'profile.html',context)
    def post(self,request):
        us = request.user
        email_new = request.POST.get('email')
        firstname_new = request.POST.get('first_name')
        lastname_new = request.POST.get('last_name')
        phone_new = request.POST.get('phone')
        address_new = request.POST.get('address')
        us.email = email_new
        us.first_name = firstname_new
        us.last_name = lastname_new
        us.phone_number =phone_new
        us.address = address_new
        us.save()
        context = {
            'us': us,
            'mess':'Thành Công!'
        }
        return render(request,'profile.html',context)

class formView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        hangsx = HangSanXuat.objects.all()
        context = {'hangsx':hangsx}
        return render(request,'form.html',context=context)
    def post(self,request):
        tenhang = request.POST.get('tenhang')
        giatien = request.POST.get('giatien')
        hsx = request.POST.get('hangsx')
        hangsx = HangSanXuat.objects.get(id = hsx)
        SmartPhone.objects.create(name= tenhang,price=giatien,hang=hangsx)
        hangsanxuat = HangSanXuat.objects.all()
        context = {
            'hangsx': hangsanxuat,
            'mess' :'Thêm Thành Công!!!'
        }
        return render(request,'form.html',context=context)
class contactsView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        nhanvien = NhanVien.objects.all().filter(id__gt =9)
        context = {
            'nv':nhanvien
        }
        return render(request,'contacts.html',context=context)
