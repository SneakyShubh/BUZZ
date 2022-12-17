from django.contrib import admin
from django.urls import path
from SocialX import views
from django.views.generic import RedirectView


urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('about/',views.about,name='index'),
    path('login/',views.login,name='index'),
    path('logout/',views.logout,name='index'),
    path('signup/',views.signup,name='index'),
    path('login/profilepic/',views.profile_pic,name='index'),
]
