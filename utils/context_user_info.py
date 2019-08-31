

def user_info(request):
    userinfo = request.session.get('userinfo')
    if userinfo:
        print(userinfo)
        return userinfo
    else:
        return {}