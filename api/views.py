from django.shortcuts import render, redirect
from testcases.models import Testcases
from .models import Api
from object.models import Objcets
from product.models import Products
from utils import baseUtils


def api_list(request):
    testcases = Testcases.objects.filter(object_id__object_state=1)
    all_api = Api.objects.all()


    return render(request, 'apilist.html', {'testcases': testcases, 'all_api': all_api})


def create_api(request, testcase_id):
    testcase = Testcases.objects.get(id=testcase_id)
    return render(request, 'createapi.html', {'testcase': testcase})


def submit_api(request, testcase_id):

    api_name = request.POST['name']
    api_url = request.POST['apiurl']
    api_method = request.POST['method']
    use_or_not = request.POST['useornot']
    api_agreement = request.POST['agreement']
    api_describe = request.POST['describe']


    api_para = dict(request.POST)
    paras = {key: value for key, value in zip(api_para['paraname[]'], api_para['paravalue[]'])}
    api = Api(testcase_id_id=testcase_id, name=api_name, api_url=api_url, method=api_method, state=use_or_not, agreement=api_agreement, describe=api_describe, parameter=paras)
    api.save()
    return redirect('apilist')

def edit_api(request, api_id):
    api = Api.objects.get(id=api_id)
    testcase = Testcases.objects.get(id=api.testcase_id_id)
    param = eval(api.parameter)

    return render(request, 'editapi.html', {'api': api, 'testcase': testcase, 'param': param})

def update_api(request, api_id):
    api = Api.objects.get(id=api_id)
    api_name = request.POST['name']
    api_url = request.POST['apiurl']
    api_method = request.POST['method']
    use_or_not = request.POST['useornot']
    api_agreement = request.POST['agreement']
    api_describe = request.POST['describe']

    api_para = dict(request.POST)
    paras = {key: value for key, value in zip(api_para['paraname[]'], api_para['paravalue[]'])}
    api.name = api_name
    api.api_url = api_url
    api.method = api_method
    api.state = use_or_not
    api.agreement = api_agreement
    api.describe = api_describe
    api.parameter = paras
    api.save()
    return redirect('apilist')


def del_api(request, api_id):
    api = Api.objects.get(id=api_id)
    api.state = 0

    api.save()
    return redirect('apilist')


def run_api(request, api_id):
    api = Api.objects.get(id=api_id)
    object = Objcets.objects.filter(products__testcases__api__exact=api_id)
    product = Products.objects.get(testcases__api__exact=api_id)

    http_request = baseUtils.ConfigHttp()
    http_request.set_url(api.agreement, product.url, api.api_url)

    # 判断参数里面是否有变量
    parameter = eval(api.parameter)
    for each_key in parameter.keys():
        if parameter[each_key].startswith('{') and parameter[each_key].endswith('}'):
            replace_str = parameter[each_key][1:-1]
            parameter[each_key] = request.session.pop(replace_str)
    print(parameter)

    http_request.set_data(parameter)
    http_request.set_re_name(api.re_name)
    http_request.set_re_value(api.re_func)
    if api.assert_info:
        http_request.set_assert_info(api.assert_info)
    else:
        assertion = None
    api_name = api.name
    api_method = api.method

    if api_method == 'GET':
        response = http_request.get()
        # print(response)
    elif api_method == 'POST':
        response = http_request.post()
        # print(response.headers)

    if api.assert_info:
        if http_request.assertion():
            assertion = {'result': True, 'info': '校验成功'}
        else:
            assertion = {'result': False, 'info': '校验失败'}

    if api.re_func and api.re_name:
        result = http_request.re_func()
        request.session[http_request.re_name] = result
    else:
        result = None


    return render(request, 'response.html', {'response': (api,response), 'assertion': assertion})


def assert_content(request, api_id):
    assert_info = request.POST['assertion']
    api = Api.objects.get(id=api_id)
    api.assert_info = assert_info
    api.save()
    return redirect('apilist')


def re_func(request, api_id):
    api = Api.objects.get(id=api_id)
    re_name = request.POST['para-name']
    re_value = request.POST['re-func']
    api.re_func = re_value
    api.re_name = re_name
    api.save()
    return redirect('apilist')