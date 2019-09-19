from django.urls import path
from .views import task_list, exe_testcases

urlpatterns = [
    path('', task_list, name='tasklist'),
    path('exetestcases/<productid>', exe_testcases, name='exetestcases')
]