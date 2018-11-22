from django.shortcuts import render,redirect
from django.urls import reverse #直接传入url
from django.views import View
from django.contrib import auth
from .forms import LoginForm,RegisteredForm
# Create your views here.

class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        return render(request, 'login_or_registered.html',{
            'login_form': login_form,
        })
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():#是否规范
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)#和数据库账号密码是否相同
            if user is not None:#有此用户
                auth.login(request, user)
                return redirect(reverse('index'))#登录成功重定向到 首页
            else:
                return render(request, 'login_or_registered.html',{
                    'errors': '账号或者密码错误',
                    'login_form': login_form
                })
        else:
            return render(request, 'login_or_registered.html',{
                    'errors': '输入错误',
                    'login_form': login_form
                })

#注册
class RegisteredView(View):
    def get(self, request):
        registered_form = RegisteredForm()
        return render(request, 'login_or_registered.html',{
            'registered_form': registered_form,
        })
    def post(self, request):
        pass



