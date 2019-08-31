from django.urls import path
from .views import edit_product, del_product, update_product

urlpatterns = [
    path('editproduct/<object_id>/<product_id>', edit_product, name='editproduct'),
    path('delproduct/<product_id>', del_product, name='delproduct'),
    path('updateproduct', update_product, name='updateproduct')

]