from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index_qlnhanvien.as_view(),name= 'qlnhanvien' ),
    path('add/',views.addnhanvienView.as_view(),name= 'addnhanvien' ),
    path('profile/<int:id>/',views.profileView.as_view(),name='xemnhanvien'),
    path('edit/<int:id>/',views.editnhanvienView.as_view(),name='editnhanvien'),
    path('xoanhanvien',views.xoanhanvien.as_view()),
]