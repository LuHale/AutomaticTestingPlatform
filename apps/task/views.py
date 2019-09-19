from django.shortcuts import render
from apps.testcases.models import Testcases
from apps.product.models import Products
from apps.object.models import Objcets
from utils.run_api import run_api
import time
from django.http import FileResponse
from utils.save_result import save_result
from .models import Task


def result_save(request):
    file = open('result.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="result.html"'
    return response

def task_list(request):
    object_testcases = []
    execute_objects = Objcets.objects.filter(object_state=1)

    # 方法一：使用多次查询对测试用例按照产品名称进行分组

    for each_object in execute_objects:
        execute_products = each_object.products_set.filter(object_id_id=each_object.id, state=1)
        for each_product in execute_products:
            execute_cases = each_product.testcases_set.filter(product_id_id=each_product.id, state=1)
            object_testcases.append((each_object, each_product, execute_cases))

    # 方法二：使用select_related方法，获取测试用例相关联的产品名称和项目名称，但是导致不能以产品进行分组

    tcs = Testcases.objects.filter(state=1, product_id__state=1, object_id__object_state=1).select_related(
        "product_id__object_id")
    # print(tcs)
    return render(request, 'tasklist.html', {'objects': object_testcases})


def exe_testcases(request, productid):

    exe_cases = Products.objects.get(pk=productid).testcases_set.filter(state=1)
    print("^"*30, exe_cases)
    product = Products.objects.get(pk=productid)
    object_id = product.object_id_id

    # 分别执行每个用例下面的每个接口
    response_list = []
    looptimes = int(request.POST.get('loopnumber'))
    intervaltime = int(request.POST.get('intervaltime'))
    exe_time = request.POST.get('exe_time')

    if exe_time:
        print(exe_time)
        # 如果设置了执行时间，则保存需要执行的用例到task库
        exe_cases_id = [each_case.id for each_case in exe_cases]
        print(exe_cases_id)
        task = Task(object_id=object_id, product_id=productid, testcases=exe_cases_id, execute_ways=3, time=exe_time)
        task.save()

    elif looptimes:
        while looptimes:
            for each_case in exe_cases:

                for each_api in each_case.api_set.filter(state=1):    # 获取所要执行的api的id

                    response_list.append(run_api(request, each_api.id))

            looptimes -= 1
            time.sleep(intervaltime)
        print(response_list)
        save_result(render(request, 'batch-response.html', {'response': response_list, 'product': product}))

    return render(request, 'batch-response.html', {'response': response_list, 'product': product})




