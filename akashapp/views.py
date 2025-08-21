from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def bedroom2bhk(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')   # 👈 redirect to new page
        else:
            return render(request, 'index.html', {'message': 'Invalid username or password!'})

    return render(request, 'index.html')


def welcome_page(request):
    return render(request, 'welcome.html')
