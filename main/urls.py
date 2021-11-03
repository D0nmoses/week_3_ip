from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    re_path(r'^profile/(\d+)', views.profile, name="profile"),
    re_path(r'^create/project', views.new_project, name="new-project"),
    re_path(r'^project/(\d+)', views.project, name="project"),
    path("search_results", views.search_results, name="search_results"),
]