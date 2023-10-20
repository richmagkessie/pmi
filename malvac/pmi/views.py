from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
from django.views import View

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .models import Community, CommunityData

from .user_communities import user_communities

# Create your views here.
@login_required(login_url = '/login/')
def home(request):
    communities = Community.objects.all()
    return render(request, 'views/home.html', {'communities': communities})


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            community = login_form.cleaned_data.get('community')
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('data')
            else:
                messages.error(request, f'An error occurred while trying to login')
        else: 
            messages.error(request, f'An error occurred while trying to login')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form,}, )


@login_required(login_url = '/login/')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def data(request):
    communities = Community.objects.all()
    community_data = {}
    for community in communities:
        data = CommunityData.objects.filter(community=community)
        community_data[community] = data 
    return render(request, 'views/data_download.html', {'community_data': community_data,  'user_communities': user_communities,})

