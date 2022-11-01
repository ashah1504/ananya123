from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    
    #Project Urls
    path("projects/", views.project, name ="projects"),
    path("projectDetails/<str:hm>/", views.projectDetails, name ="details"),
    path("projectAdd/", views.projectAdd, name="projectAdd"),
    path("projectDelete/<str:id>/",views.projectDelete, name="projectDelete"),
    path("projectUpdate/<str:id>/", views.projectUpdate, name="projectUpdate"),
    
    #CV urls
    path("cv/", views.cv, name="cv"),
    path("hireMe/", views.hireMe, name ="hireMe"),
    
    
]