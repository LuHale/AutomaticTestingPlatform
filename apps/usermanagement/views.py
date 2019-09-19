from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from django.db.models import F


class GroupManagement(ListView):
    model = Group  # 对应的模型名称
    template_name = 'groupmanagement.html'  # 对应的模板
    paginate_by = 20  # 每页显示条数
    context_object_name = 'groups'  # 模板引用上下文时使用的名称
    ordering = 'id'  # 根据id排序
    page_kwarg = 'p'  # 页码参数

    # def get_context_data(self, **kwargs):
    #     context = super(GroupManagement, self).get_context_data(**kwargs)

    def get_queryset(self):
        # print("-*"*40, Group.objects.all())
        group_list = Group.objects.filter(group_extension__group_state=1)

        return group_list


class CreateGroup(View):
    """创建组"""
    def get(self, request, *args, **kwargs):
        # user = request.user
        # print(type(user))
        # user = request.session.items()
        # user = request.session.get()
        permissions = Permission.objects.filter().order_by('id')
        return render(request, 'creategroup.html', {'permissions': permissions})

    def post(self, request, *args, **kwargs):
        userid = request.user.id    # 获取登录用户的id
        user = User.objects.get(id=userid)
        group_name = request.POST.get('group_name')
        group = Group.objects.create(name=group_name)    # 创建组
        group.group_extension.create_user = user
        group_right = request.POST.getlist('group_right')
        permissions = Permission.objects.filter(codename__in=group_right)    # 把需要添加的权限转换为queryset
        group.permissions.set(permissions)    # 为组添加权限
        group.save()
        return redirect('usermanagement:groups_list')


class EditGroup(View):
    def get(self, request, groupid, *args, **kwargs):
        editgroup = Group.objects.get(id=groupid)
        permissions = Permission.objects.filter().order_by('id')

        return render(request, 'edit-group.html', {'group': editgroup, 'permissions': permissions})

    def post(self, request, groupid, *args, **kwargs):
        userid = request.user.id  # 获取登录用户的id
        user = User.objects.get(id=userid)
        group_name = request.POST.get('group_name')
        group = Group.objects.get(id=groupid)
        group.group_extension.create_user = user
        group_right = request.POST.getlist('group_right')
        permissions = Permission.objects.filter(codename__in=group_right)  # 把需要添加的权限转换为queryset
        group.permissions.set(permissions)  # 为组添加权限
        group.save()
        return redirect('usermanagement:groups_list')

class DelGroup(View):
    def get(self, request, groupid, *args, **kwargs):
        group = Group.objects.get(id=groupid)
        group.group_extension.group_state = False
        group.save()
        group_list = Group.objects.filter(group_extension__group_state=1)
        return render(request, 'groupmanagement.html', {'groups': group_list})

class AddUser(View):
    """向用户组添加用户"""
    def get(self, request, groupid, *args, **kwargs):
        group = Group.objects.get(id=groupid)
        user_list = group.user_set.all()
        print(user_list)
        return render(request, 'add-user.html', {'users': user_list, 'group': group})

    def post(self, request, groupid, *args, **kwargs):
        group = Group.objects.get(id=groupid)
        users_id = request.POST.get('users_id')
        user_name = request.POST.get('user_name')
        if user_name:
            add_user = User.objects.get(username=user_name)
            add_user.groups.add(group)


        return redirect('usermanagement:groups_list')

class DelUser(View):
    """从用户组删除用户"""
    def get(self, request, groupid, userid):
        group = Group.objects.get(id=groupid)
        user = User.objects.get(id=userid)
        user.groups.remove(group)
        return redirect('usermanagement:user_add', groupid)

class UserManagement(ListView):
    model = User  # 对应的模型名称
    template_name = 'usermanagement.html'  # 对应的模板
    paginate_by = 20  # 每页显示条数
    context_object_name = 'users'  # 模板引用上下文时使用的名称
    ordering = 'id'  # 根据id排序
    page_kwarg = 'p'  # 页码参数

    # def get_context_data(self, **kwargs):
    #     context = super(GroupManagement, self).get_context_data(**kwargs)

    # 获取上下文数据
    def get_context_data(self, **kwargs):
        context = super(UserManagement, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pages = self.get_pagination_data(paginator, page_obj, 2)
        context.update(pages)
        return context

    def get_queryset(self):
        # print("-*"*40, Group.objects.all())
        user_list = User.objects.filter()

        return user_list

    # 生成页码
    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        count_page = paginator.num_pages
        left_has_more = False
        right_has_more = False
        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)
        if current_page >= count_page - around_count - 1:
            right_pages = range(current_page + 1, count_page + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': count_page
        }

class UserGroupManage(View):
    """管理用户名下的用户组"""
    def get(self, request, userid, *args, **kwargs):
        user = User.objects.get(id=userid)
        group_list = user.groups.all()
        print(group_list)
        return render(request, 'user-groups-manage.html', {'user': user, 'groups': group_list})

    def post(self, request, userid, *args, **kwargs):
        user = User.objects.get(id=userid)
        group_name = request.POST.get('group_name')
        if group_name:
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
        return redirect('usermanagement:user_list')

class UserDelGroup(DelUser):
    """从用户管理删除用户加入的组"""
    def get(self, request, groupid, userid):
        super(UserDelGroup, self).get(request, groupid, userid)
        return redirect('usermanagement:manage_group', userid)

class UserEnableOrForbidden(View):
    """用户禁用和启用"""
    def get(self, request, userid, operateid, *args, **kwargs):
        user = User.objects.get(id=userid)
        if operateid == '1' and user.is_active is False:    # 1为启用
            user.is_active = 1
        elif operateid == '2' and user.is_active:    # 2为禁用
            user.is_active = 0
        user.save()
        return redirect('usermanagement:user_list')