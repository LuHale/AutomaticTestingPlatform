from django.urls import path
from .views import create_object, submit_object, search_object, ObjectList, SearchObject

app_name = 'object'

urlpatterns = [
    path('', create_object, name='createobject'),
    path('submitobject/', submit_object, name='submitobject'),
    # path('searchobject/', search_object, name='searchobject'),
    path('searchobject/', SearchObject.as_view(), name='searchobject'),
    path('objectlist', ObjectList.as_view(), name='objectlist')
]