from django.shortcuts import render, redirect
from object.models import Objcets
from product.models import Products
from .models import Testcases


def testcaselist(request):

    objects = Objcets.objects.filter(object_state='1')
    products = Products.objects.filter(object_id_id__in=objects, state='1')
    testcases = Testcases.objects.filter(object_id_id__in=objects, product_id_id__in=products).values()

    if testcases:
        for eachtestcase in testcases:
            object_name = objects.get(id=eachtestcase['object_id_id']).object_name
            product_name = products.get(id=eachtestcase['product_id_id']).name
            eachtestcase['object_name'] = object_name
            eachtestcase['product_name'] = product_name

    return render(request, 'testcase.html', {"context": testcases})


def del_testcase(request, testcase_id):
    if testcase_id:
        testcase = Testcases.objects.get(id=testcase_id)
        testcase.state = 0
        testcase.save()
    return redirect('testcaselist')


def create_testcase(request):
    # 先获取所有的项目和产品的名称、id，传递给下拉选择框，项目和产品有关联性
    objects = Objcets.objects.filter(object_state='1')
    products = Products.objects.filter(object_id_id__in=objects, state='1')

    return render(request, 'createtestcase.html', {'products': products, 'objects': objects})


def submit_testcase(request):
    if request.method == 'POST':
        object_id = request.POST['objectid']
        product_id = request.POST['productid']
        testcase_name = request.POST['testcasename']
        testcase_describe = request.POST['testcasedescribe']

        if object_id and product_id and testcase_name:
            testcase = Testcases(name=testcase_name, describe=testcase_describe, object_id_id=object_id, product_id_id=product_id)
            testcase.save()
    return redirect('testcaselist')


def edit_testcase(request, object_id, product_id, testcase_id):
    if object_id and product_id and testcase_id:
        object = Objcets.objects.get(id=object_id)
        product = Products.objects.get(id=product_id)
        testcase = Testcases.objects.get(id=testcase_id)
        print(object, product, testcase)
        objects = Objcets.objects.filter(object_state='1').exclude(id=object_id)
        products = Products.objects.filter(object_id_id__in=objects, state='1').exclude(id=product_id)

        request.session['testcase_id'] = testcase_id


    return render(request, 'edittestcase.html', {'object':object, 'product':product, 'testcase':testcase, 'objects':objects, 'products':products})


def update_testcase(request):
    if request.method == 'POST':
        object_id = request.POST['objectid']
        product_id = request.POST['productid']
        testcase_name = request.POST['testcasename']
        testcase_describe = request.POST['testcasedescribe']

        if object_id and product_id and testcase_name:
            testcase_id = request.session.pop('testcase_id')
            testcase = Testcases.objects.get(id=testcase_id)
            testcase.object_id_id = object_id
            testcase.product_id_id = product_id
            testcase.name = testcase_name
            testcase.describe = testcase_describe
            testcase.save()
    return redirect('testcaselist')