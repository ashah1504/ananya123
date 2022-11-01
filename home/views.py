from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from . models import SpecialSkills, Project
from . forms import ProjectForms

# Create your views here.
def home(request):
    try: 
        data = SpecialSkills.objects.all()
        context = {"special":data}
    except Exception as e:
        context = {"special":"Data Not Found"}
    return render(request, 'index.html', context)

def project(request):
    try: 
        data = Project.objects.all()
        context = {"project":data}
    except Exception as e:
        context = {"project":"Data Not Found"}
    return render(request, 'projects.html', context)

def projectDetails(request, hm):
    # fetch_data = Project.objects.filter(name=hm)
    fetch_data = Project.objects.get(name=hm)
    context = {"fetch_data":fetch_data}
    return render(request, 'projectDetails.html', context)

@login_required(login_url="login_page")
@permission_required('home.add_project', login_url="home")
def projectAdd(request):
    form = ProjectForms()
    if request.method == 'POST':
        myData = ProjectForms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request, 'Project Added Successfully')
            return redirect('projects')
    context = {"form":form}
    return render(request, 'projectAdd.html', context)

@login_required(login_url="login_page")
@permission_required('home.delete_project', login_url="home")

def projectDelete(request, id):
    data = Project.objects.get(id=id)
    data.delete()
    messages.warning(request, 'Project Deleted Successfully')
    return redirect('projects')

@login_required(login_url="login_page")
@permission_required('home.update_project', login_url="home")
def projectUpdate(request,id):
    myData = Project.objects.get(id=id)
    updateForm = ProjectForms(request.POST or None, instance=myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Project Updated Successfully')
        return redirect("projects")
    context = {"form":updateForm} 
    return render(request, 'projectUpdate.html',context)

def cv(request): 
    return render(request, 'cv.html')

def hireMe(request): 
    return render(request, 'hireMe.html')    

