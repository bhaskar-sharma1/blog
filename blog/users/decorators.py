from django.shortcuts import redirect

def to_home_page(function):
    '''
    THIS DECORATOR REDIRECT USER TO HOME PAGE 
    IN CASE HE ALREADY LOGGED IN..
    '''
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return function(request, *args, **kwargs)
    return wrap