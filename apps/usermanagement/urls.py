from django.urls import path
from . import views

app_name = "usermanagement"


urlpatterns = [
    path('', views.GroupManagement.as_view(), name='groups_list'),
    path('create_group/', views.CreateGroup.as_view(), name='create_group'),
    path('edit_group/<groupid>/', views.EditGroup.as_view(), name='edit_group'),
    path('del_group/<groupid>', views.DelGroup.as_view(), name='del_group'),
    path('user_list/', views.UserManagement.as_view(), name='user_list'),
    path('add_user/<groupid>', views.AddUser.as_view(), name='user_add'),
    path('del_user/<groupid>/<userid>', views.DelUser.as_view(), name='del_user'),
    path('user_del_group/<groupid>/<userid>', views.UserDelGroup.as_view(), name='user_del_group'),
    path('manage_group/<userid>', views.UserGroupManage.as_view(), name='manage_group'),
    path('user_state/<userid>/<operateid>', views.UserEnableOrForbidden.as_view(), name='user_state')
]