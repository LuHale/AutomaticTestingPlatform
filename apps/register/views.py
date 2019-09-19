from django.shortcuts import redirect, reverse, render
from .models import User
from apps.front.views import front
from django.views import View
from .forms import RegisterForm


# 视图函数
# def register_page(request):
#     return render(request, 'page-register.html')
#
#
# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         phonenum = request.POST['phone']
#
#         if username and email and password and phonenum:
#             user = User(name=username, pwd=password, email=email, phone_number=phonenum)
#             user.save()
#             return redirect(reverse(front))    # 页面重定向到首页


# 类视图
# class Register(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'page-register.html')
#
#     def post(self, request):
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         phonenum = request.POST['phone']
#
#         if username and email and password and phonenum:
#             user = User(name=username, pwd=password, email=email, phone_number=phonenum)
#             user.save()
#             return redirect(reverse(front))  # 页面重定向到首页

# 视图表单
class Register(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'page-register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.extension.phone_number = phone_number    # 向扩展表添加数据
            user.save()

            return redirect(reverse(front))  # 页面重定向到首页
        else:
            print(form.errors.get_json_data())
            return render(request, 'page-register.html')