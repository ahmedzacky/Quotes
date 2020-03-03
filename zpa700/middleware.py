from accounts.forms import LoginForm


def login_navbar_middleware(get_response):
    def middleware(request):
        # attach the login form to the request object for further rendering ino navbar
        form = LoginForm()
        request.login_form = form
        response = get_response(request)
        return response

    return middleware
