from django.core.exceptions import PermissionDenied


def is_employer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'employer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def is_employee(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'employee':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
