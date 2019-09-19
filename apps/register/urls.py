from django.urls import path
from .views import Register


urlpatterns = [
    # path('', register_page, name='register'),
    path('', Register.as_view(), name='register'),
    # path('signup/', signup, name='signup'),

]