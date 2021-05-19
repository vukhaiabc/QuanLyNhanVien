from django.urls import path
from . import views

urlpatterns = [
    path('',views.qltuyendungindex.as_view(),name='qltuyendung'),
    path('qlhopdong',views.qlhopdongView.as_view(),name='qlhopdong'),
    path('qlbonhiem',views.qlbonhiemView.as_view(),name='qlbonhiem'),
    path('qlnghiviec',views.qlnghiviecView.as_view(),name='qlnghiviec'),
    path('tintuyendung',views.tintuyendungView.as_view(),name='tintuyendung'),
    path('chitietbonhiem',views.chitietbonhiemView.as_view(),name='chitietbonhiem'),
    path('nhanviencu',views.qlnhaviencuView.as_view(),name='qlnhanviencu'),
    path('addhopdong',views.themhopdongView.as_view(),name='themhopdong'),
    path('edit/<int:id>/',views.edithopdongView.as_view(),name='edithopdong'),
    path('qlbonhiem/chitietbn/<int:id>/',views.chitietnguoibonhiemView.as_view(),name='chitietnvbonhiem'),
    path('laynhanvien',views.laynhanvien.as_view()),
    path('laymoinhanvien',views.laymoinhanvien.as_view()),
    path('xoahopdong',views.xoahopdong.as_view()),

]
