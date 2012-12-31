def login(request):
    username = request.session.get('username', None)
    login_error = request.session.get('login_error', None)
    if login_error:
        request.session.pop('login_error')
    return dict(username = username, login_error = login_error)