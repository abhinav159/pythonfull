from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def cust_auth(func):
    def warpper(request, *args, **kwargs):
        if 'customer' in request.session:
            return func(request, *args, **kwargs)#customer is the key in session
        else:
            return redirect('common:customer_login')# if the session customer is not there, thn it will redirect to login page

    return warpper