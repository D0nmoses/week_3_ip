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

            return redirect(home)

    else:

        form = NewProjectForm()

    title = 'Create Project'

    return render(request,'all-project/new_project.html', {"form":form})

@login_required(login_url='/accounts/login')
def project(request,id):
    '''	
    View function to display a single post, its comments and likes	
    '''
    current_user = request.user
    try:
        current_project = Project.objects.get(id=id)

        title = f'{current_project.user_profile.username}\'s project'


    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'all-project/project.html', {"title":title, "project":current_project })

@login_required(login_url='/accounts/login')
def search_results(request):
    project = Project.objects.all()
    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'all-project/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-project/search.html',{"message":message})
