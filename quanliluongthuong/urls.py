from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.qlluongthuongView.as_view(),name= 'qlluongthuong' ),
    path('qlluongnhanvien/',views.qlluongnhanvienView.as_view(),name= 'qlluongnhanvien' ),
    path('adduongnhanvien/',views.themluongnhanvienView.as_view(),name= 'addluongnhanvien' ),
    path('editluongnhanvien/<int:id>/',views.editluongnhanvien.as_view(),name= 'editluongnhanvien' ),
    path('qlbacluong/',views.qlbacluongView.as_view(),name= 'qlbacluong' ),
    path('qlphucap/',views.qlphucapView.as_view(),name= 'qlphucap' ),
    path('qlthuong/',views.qlthuongView.as_view(),name= 'qlthuong' ),
    path('luuphucap/',views.luuphucap.as_view()),
    path('layphucap/',views.layphucap.as_view()),
    path('capnhatphucap/',views.capnhatphucap.as_view()),
    path('xoaphucap/',views.xoaphucap.as_view()),
    path('thembacluong/',views.thembacluong.as_view()),
    path('laybacluong/',views.laybacluong.as_view()),
    path('capnhatbacluong/',views.capnhatbacluong.as_view()),
    path('xoabacluong/',views.xoabacluong.as_view()),
    path('themthuong/',views.themthuong.as_view()),
    path('laythuong/',views.laythuong.as_view()),
    path('capnhatthuong/',views.capnhatthuong.as_view()),
    path('xoathuong/',views.xoathuong.as_view()),
    path('xoaluongnhanvien/',views.xoaluongnhanvien.as_view()),
]