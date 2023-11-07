"""
URL configuration for cybbit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('posts/',views.posts,name='posts'),
    
    #AUTHENTICATION URLS
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('signup/',views.signupuser,name='signupuser'),
    
    path('createpost',views.createpost,name='createpost'),
    path('posts/<int:pk>',views.viewpost,name="viewpost"),

]

admin.site.site_header = "Cybbit Admin"
admin.site.site_title = " Cybbit Admin Portal"
admin.site.index_title = "Welcome to Cybbit Admin"