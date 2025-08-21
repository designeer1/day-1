from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def bedroom2bhk(request):
    res = {'name': 'Kalyan'}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            res['name'] = username
            res['message'] = 'Login successful!'
        else:
            res['message'] = 'Invalid username or password!'

    return render(request, 'index.html', res)
