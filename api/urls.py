from django.urls import path
from .views import api_list, create_api, submit_api, edit_api, del_api, update_api, run_api, assert_content, re_func

urlpatterns = [
    path('', api_list, name='apilist'),
    path('createapi/<testcase_id>', create_api, name='createapi'),
    path('submitapi/<testcase_id>', submit_api, name='submitapi'),
    path('editapi/<api_id>', edit_api, name='editapi'),
    path('delapi/<api_id>', del_api, name='delapi'),
    path('updateapi/<api_id>', update_api, name='updateapi'),
    path('runapi/<api_id>', run_api, name='runapi'),
    path('assert/<api_id>', assert_content, name='assert'),
    path('refunc/<api_id>', re_func, name='refunc')

]
