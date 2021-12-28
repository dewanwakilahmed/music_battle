from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'login' in request.POST:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/my-profile-tab')
            else:
                messages.info(request, 'Invalid Credentials!')
                return redirect('/')
        # elif ('register' in request.POST):
        #     if username == '' or password == '':
        #         messages.error(
        #             request, 'Please provide both username and password')
        #         return redirect('/')
        #     else:
        #         if User.objects.filter(username=username).exists():
        #             messages.info(request, 'Username Already Taken!')
        #             return redirect('/')
        #         else:
        #             user = User.objects.create_user(
        #                 username=username, password=password)
        #             user.save()
        #             messages.info(
        #                 request, 'Account Registered! Please Login Now')
        #             return redirect('/')
    else:
        return render(request, 'baseapp/index.html')

# def dashboard(request):
#     if request.user.is_authenticated:
#         return render(request, 'baseapp/dashboard.html')
#     else:
#         return redirect('/')

def myProfileTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/my-profile-tab.html')
    else:
        return redirect('/')


def guildsTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/guilds-tab.html')
    else:
        return redirect('/')


def challengesTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/challenges-tab.html')
    else:
        return redirect('/')


def buyInTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/buy-in-tab.html')
    else:
        return redirect('/')


def myTicketsTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/my-tickets-tab.html')        
    else:
        return redirect('/')


def battlesTab(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/battles-tab.html')
    else:
        return redirect('/')


def adminPanel(request):
    if request.user.is_authenticated:
        return render(request, 'baseapp/admin-panel.html')
    else:
        return redirect('/')
