from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views import View


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['user name']
#         password = request.POST['Password']
#
#         if username and password:
#             try:
#                 user = User.objects.get(name__iexact=username)
#             except:
#                 return render(request, 'page-login.html')
#             if user.pwd == password:
#                 context = {
#                     'username': username
#                 }
#                 request.session['userinfo'] = context
#                 return redirect('/homepage/')
#             else:
#                 return redirect('/index/')


# def logout(request):
#     request.session.pop('userinfo')
#     return redirect('/index/')


# class Login(View):
#
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         print(11111111111111)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             remember = form.cleaned_data.get('remember')
#             print(username, password)
#             user = authenticate(username=username, password=password)
#             print(user)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                 # context = {
#                 #     'username': form.cleaned_data.get('name')
#                 # }
#                 # request.session['userinfo'] = context
#                     if remember:
#                         request.session.set_expiry(None)    # 设置为None则表示使用全局的过期时间
#                     else:
#                         request.session.set_expiry(0)
#                 return redirect('/homepage/')
#             else:
#                 raise form.ValidationError('用户名或密码错误，请重新输入')
#
#         else:
#             print(form.errors.get_json_data())
#             return redirect('/index/')


class Login(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)    # 设置为None则表示使用全局的过期时间
                else:
                    request.session.set_expiry(0)
            else:
                print('用户已被锁定')
                return redirect('/index/')
            return redirect('/homepage/')

        else:
            return redirect('/index/')


class LogOut(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('front'))