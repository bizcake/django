from django.shortcuts import render, redirect


# index
def index(request):

    if request.user.is_authenticated:
        pass
    else:
        return redirect('account:login')

    return render(request, 'index.html')
