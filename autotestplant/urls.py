"""autotestplant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from apps.login import LogOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('apps.front.urls')),
    path('homepage/', include('apps.homepage.urls')),
    path('logout/', LogOut.as_view(), name='logout'),
    path('createobject/', include('apps.object.urls')),
    path('register/', include('apps.register.urls')),
    path('product/', include('apps.product.urls')),
    path('testcase/', include('apps.testcases.urls')),
    path('api/', include('apps.api.urls')),
    path('tasklist', include('apps.task.urls'))
]
