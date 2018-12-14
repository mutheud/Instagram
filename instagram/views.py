from django.shortcuts import render
from .forms import InstagramForm

def login(request):

    if request.method == 'POST':
        form =InstagramForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form =InstagramForm()
    return render(request, 'login.html')

def signup(request):

    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form =SignUpForm()
    return render(request, 'registration_form.html')