from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url= '/index/')
def homepage(request):
    # print(request.session.get('id'))
    # username = request.session.get('username')
    return render(request, 'front.html')


