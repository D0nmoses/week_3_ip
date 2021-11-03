from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.objects.all()

    return render(request, 'all-project/home.html',{'projects':projects})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    '''	
    View function to display the profile of the logged in user when they click on the user icon	
    '''
    current_user = request.user

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        projects = Project.objects.filter(user=current_user.id)

        return render(request, 'all-project/my_profile.html', {"title":title,"single_profile":single_profile,"current_user":current_user,"projetcs":projects})

    except ObjectDoesNotExist:
        raise Http404()

@login_required(login_url='/accounts/login/')
def new_project(request):

    
