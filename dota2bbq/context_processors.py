def login(request):
    username = None
    login_error = None
    if request.user.is_authenticated():   
        username = request.user.username
    else:
        login_error = request.session.get('login_error')
        if login_error:
            request.session.pop('login_error')
    return dict(username = username, login_error = login_error)