from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.objects.all()

    return render(request, 'all-project/home.html',{'projects':projects})
