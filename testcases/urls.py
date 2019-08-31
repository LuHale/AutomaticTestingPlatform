from django.urls import path
from.views import testcaselist, del_testcase, create_testcase, submit_testcase, edit_testcase, update_testcase


urlpatterns = [
    path('', testcaselist, name='testcaselist'),
    path('deltestcase/<testcase_id>', del_testcase, name='deltestcase'),
    path('createtestcase/', create_testcase, name='createtestcase'),
    path('submittestcase/', submit_testcase, name='submittestcase'),
    path('edittestcase/<object_id>/<product_id>/<testcase_id>', edit_testcase, name='edittestcase'),
    path('updatetestcase/', update_testcase, name='updatetestcase')
]