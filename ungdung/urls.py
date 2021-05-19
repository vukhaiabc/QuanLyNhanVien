from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.loginView.as_view(),name= 'login' ),
    path('logout/',views.logout_view,name= 'logout' ),
    path('changepassword/',views.changepasswordView.as_view(),name= 'change_password' ),
    path('profile/',views.profileView.as_view(),name= 'profile' ),
    path('registermember/',views.registermember.as_view(),name= 'register_member' ),
    path('',views.index.as_view(),name= 'index_view' ),
    path('form/',views.formView.as_view(),name= 'form_view' ),
    path('contacts/',views.contactsView.as_view(),name= 'contacts' ),
]