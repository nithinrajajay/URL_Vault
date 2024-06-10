from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signuppage'),
    path('signin/',views.signin,name='signinpage'),
    path('signout/',views.signout,name='signoutpage'),
    path('addurl/',views.addurl,name='addurlpage'),
    path('listurl/',views.listurl,name='listurlpage'),
    path('editurl/<int:id>/',views.editurl,name='editurlpage'),
    path('deleteurl/<int:id>/',views.deleteurl,name='deleteurlpage'),
    
]