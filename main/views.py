from django.shortcuts import render
from .models import Project, Profile

# Create your views here.
def home(request):
    projects = Project.objects.all()

    return render(request, '')
