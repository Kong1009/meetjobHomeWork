"""comprehensive_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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



from movies.views import all_movies
from cartoon.views import all_cartoon
from members.views import member_manage, register, login, logout
from shop.views import CarStore, MotoStore, GroceryStore, GameStore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_cartoon),
    
    # 動漫區
    path('all_cartoon/', all_cartoon),
    
    # 電影區
    path('all_movie/', all_movies),
    
    # 會員專區
    path('member_manage/', member_manage),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    
    # 商店
    path('game/', GameStore),
    path('car/', CarStore),
    path('moto/', MotoStore),
    path('grocery/', GroceryStore),
    
]
