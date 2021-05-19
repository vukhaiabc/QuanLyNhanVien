from django.urls import path
from . import views

urlpatterns = [
    path('',views.qldaotaoView.as_view(),name='qldaotao'),
    path('chitiet/<int:id>/',views.chitietmotkhoahoc.as_view(),name='chitietkhoahoc'),
    path('addkhnhanvien/',views.addkhnhanvien.as_view(),name= 'nhanvienkh'),
    path('themkhoahoc/',views.themkhoahoc.as_view()),
]
