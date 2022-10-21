from django.shortcuts import render,redirect

def auth_user(func):
    def wrap(request, *args, **kwargs):
        if 'mysession' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')
            
    return wrap