"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path,include
from django.views.static import serve
import xadmin
from .settings import MEDIA_ROOT
from .views import index
from user.views import UserAvatarView,AvatarAjaxView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    #图片上传URL
    re_path('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('', index, name="index"),#主页
    path('operation/', include('operation.urls')),#用户操作

    # 帖子URL
    path('forum/', include('userforum.urls')),

    #展示用户头像
    path('avatar/',UserAvatarView.as_view(),name="avatar"),

    #上传用户头像更新
    path('avatar/ajax',AvatarAjaxView.as_view(),name="avatar_ajax")
]
