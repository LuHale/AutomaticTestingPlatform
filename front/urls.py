from django.urls import path
from .views import front
from login.views import Login

urlpatterns = [
    path('', front, name='front'),
    # path('register/', register_page, name='register'),
    # path('signup/', signup, name='signup'),
    path('login/', Login.as_view(), name='login'),
]