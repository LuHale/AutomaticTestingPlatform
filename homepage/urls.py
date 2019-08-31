from django.urls import path
from homepage import views
from object.views import del_object, edit_object, edit_sbumit
from product.views import create_product, submit_prodect

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('delobject/<object_id>/', del_object, name="delobject"),
    path('editobject/<object_id>', edit_object, name="editobject"),
    path('editobject/editsubmit/<id>', edit_sbumit, name='editsubmit'),
    path('createproduct/<object_id>', create_product, name='createproduct'),
    path('createproduct/submitproduct/', submit_prodect, name='submitproduct'),

]
