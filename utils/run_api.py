from apps.api.models import Api
from apps.object.models import Objcets
from apps.product.models import Products
from .baseUtils import ConfigHttp


def run_api(request, api_id):
    api = Api.objects.get(id=api_id)
    object = Objcets.objects.filter(products__testcases__api__exact=api_id)
    product = Products.objects.get(testcases__api__exact=api_id)

    http_request = ConfigHttp()
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
        print(response)
    elif api_method == 'POST':
        response = http_request.post()
        print(response.headers)

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


    return {'response': (api, response), 'assertion': assertion}