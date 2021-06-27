"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.htmltag),
    path('usr/<str:uname>/',views.usernameprint),
    path('usag/<str:un>/<int:ag>/',views.usernameage),
    path('emp/<str:eid>/<int:eage>/<str:ename>/',views.empdetails),
    path('qw/',views.html),
    path('yt/<str:name>/',views.ytname),
    path('pt/<int:id>/<str:name>/',views.employ),
    path('abc/<int:id>/<str:name>/',views.employ01),
    path('stud/',views.studentdetails),
    path('internalJS/',views.internalJS),
    path('myform/',views.myform,name='myform1'),
    path('registration/',views.registration,name='my registration'),
    path('loginpage/',views.loginpage,name='my login'),
    path('btstrp',views.bootstarpfun),
    path('newreg/',views.newreg),
    path('newlog/',views.newlog),
    path('btregi/',views.btregst,name="btr"),
    path('sandeep/',views.sandeep),
    path('register1/',views.register1),
    path('register/',views.register2,name="register2"),
    path('display/',views.display,name='dt'),
    path('viw/<int:y>/',views.sview,name="sv"),
    path('upu/<int:q>/',views.supt,name="sup"),
    path('dl/<int:p>/',views.sudl,name="sd"),
]