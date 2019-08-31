from django.shortcuts import render, redirect
from object.models import Objcets
from .models import Products


def create_product(request, object_id):
    object = Objcets.objects.get(id=object_id)
    request.session['object_id'] = object_id
    return render(request, 'createproduct.html', {'object': object})


def submit_prodect(request):
    if request.method == 'POST':
        product_name = request.POST['productname']
        product_url = request.POST['producturl']
        product_describe = request.POST['productdescribe']
        product_object_id_id = request.session.pop('object_id')

    if product_name and product_url:
        product = Products(name=product_name, url=product_url, describe=product_describe, object_id_id=product_object_id_id)
        product.save()
    return redirect('object:objectlist')


def edit_product(request, object_id, product_id):
    request.session['product_id'] = product_id
    object_name = Objcets.objects.get(id=object_id).object_name
    product = Products.objects.get(id=product_id)
    context = {}
    context['object_name'] = object_name
    context['product'] = product
    return render(request, 'editproduct.html', context)


def update_product(request):
    if request.method == 'POST':
        product_name = request.POST['productname']
        product_url = request.POST['producturl']
        product_describe = request.POST['productdescribe']
        # product_object_id_id = request.session.pop('object_id')
        product_id = request.session.pop('product_id')

    if product_name and product_url and product_id:
        product = Products.objects.get(id=product_id)
        product.name = product_name
        product.url = product_url
        product.describe = product_describe
        product.save()
    return redirect('object:objectlist')


def del_product(request, product_id):
    product = Products.objects.get(id=product_id)
    product.state = 0
    product.save()
    return redirect('object:objectlist')