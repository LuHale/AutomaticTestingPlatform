from django.shortcuts import render, redirect
from .models import Objcets
from django.db.models import F, Q
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='/login/')
def create_object(request):
    return render(request, 'creatobject.html')


def submit_object(request):
    if request.method == "POST":
        object_name = request.POST['objectname']
        object_describe = request.POST['objectdescribe']

    if object_name:
        object = Objcets(object_name=object_name, object_describe=object_describe)
        object.save()
        return redirect('object:objectlist')


@login_required(login_url='/login/')
def del_object(request, object_id):
    object = Objcets.objects.get(id=object_id)
    object.object_state = 0
    object.save()
    return redirect('object:objectlist')


@login_required(login_url='/login/')
def edit_object(request, object_id):
    object = Objcets.objects.get(id=object_id)
    return render(request, 'editobject.html', {"object": object})


def edit_sbumit(request, id):
    object = Objcets.objects.get(id=id)
    object.object_name = request.POST['objectname']
    object.object_describe = request.POST['objectdescribe']
    object.save()
    return redirect('objectlist')


def search_object(request):
    """按照项目名称搜索项目"""
    search_text = request.POST.get('searchobjectname')

    # 获取分别获取项目下的产品，但是这个语句没有过滤掉已经删除的产品，需要修改
    search_result = Objcets.objects.filter(object_name__contains=search_text, object_state=1).annotate(search_product=F('products__object_id_id')).distinct()

    return render(request, 'objectlist.html', {"objects": search_result})


class ObjectList(ListView):
    model = Objcets    # 对应的模型名称
    template_name = 'objectlist.html'    # 对应的模板
    paginate_by = 10    # 每页显示条数
    context_object_name = 'objects'    # 模板引用上下文时使用的名称
    ordering = 'id'    # 根据id排序
    page_kwarg = 'p'    # 页码参数

    # 获取上下文数据
    def get_context_data(self, **kwargs):
        context = super(ObjectList, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pages = self.get_pagination_data(paginator, page_obj, 2)
        context.update(pages)
        return context

    # 重新生成查询语句
    def get_queryset(self):
        print("*"*40, Objcets.objects.filter(object_state=1))
        return Objcets.objects.filter(object_state=1).annotate(search_product=F('products__object_id_id')).distinct()

    def post(self, request, *args, **kwargs):
        search_text = request.POST.get('searchobjectname')
        if search_text:
            objects = Objcets.objects.filter(object_name__contains=search_text, object_state=1).annotate(search_product=F('products__object_id_id')).distinct()
        else:
            objects = self.get_queryset()
        context = self.get_context_data(object_list=objects)
        return render(request, 'objectlist.html', context)

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
            left_pages = range(current_page-around_count, current_page)
        if current_page >= count_page - around_count-1:
            right_pages = range(current_page+1, count_page+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': count_page
        }


class SearchObject(ListView):
    model = Objcets    # 对应的模型名称
    template_name = 'search-object.html'    # 对应的模板
    paginate_by = 10    # 每页显示条数
    context_object_name = 'objects'    # 模板引用上下文时使用的名称
    ordering = 'id'    # 根据id排序
    page_kwarg = 'p'    # 页码参数

    # 获取上下文数据
    def get_context_data(self, **kwargs):
        context = super(SearchObject, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pages = self.get_pagination_data(paginator, page_obj, 2)
        context.update(pages)
        return context

    # 重新生成查询语句
    def get_queryset(self):
        print("*"*40, Objcets.objects.filter(object_state=1))
        return Objcets.objects.filter(object_state=1).annotate(search_product=F('products__object_id_id')).distinct()

    def post(self, request, *args, **kwargs):
        search_text = request.POST.get('searchobjectname')
        if search_text:
            objects = Objcets.objects.filter(object_name__contains=search_text, object_state=1).annotate(
                search_product=F('products__object_id_id')).distinct()
        else:
            objects = self.get_queryset()
        context = self.get_context_data(object_list=objects)
        context.update(kw=search_text)
        return render(request, 'search-object.html', context)

    def get(self, request, *args, **kwargs):
        search_text = request.GET.get('searchobject')
        if search_text:
            objects = Objcets.objects.filter(object_name__contains=search_text, object_state=1).annotate(
                search_product=F('products__object_id_id')).distinct()
        else:
            objects = self.get_queryset()
        context = self.get_context_data(object_list=objects)
        context.update(kw=search_text)
        return render(request, 'search-object.html', context)

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
            left_pages = range(current_page-around_count, current_page)
        if current_page >= count_page - around_count-1:
            right_pages = range(current_page+1, count_page+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': count_page
        }