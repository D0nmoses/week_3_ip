from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewProjectForm


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

    current_user = request.user

    current_profile = current_user.profile

    if request.method == 'POST':

        form = NewProjectForm(request.POST, request.FILES)

        if form.is_valid:

            project = form.save(commit=False)

            project.user = current_user

            project.profile = current_profile

            project.save()

            return redirect(profile, current_user.id)

    else:

        form = NewProjectForm()

    title = 'Create Post'

    return render(request,'all-posts/new_post.html', {"form":form})
