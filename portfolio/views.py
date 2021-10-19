from django.shortcuts import render, redirect
from django.http import HttpResponse

from portfolio.forms import projForm
from .models import Project
from django.template import loader

# Create your views here.
def index(request):
    projList = Project.objects.all()
    context = {
        'projList': projList,
    }
    return render(request, 'project/index.html', context)

def detail(request, projectId):
    project = Project.objects.get(pk=projectId)
    context = {
        'project': project
    }
    return render(request, 'project/detail.html', context)

    
def createProj(request):
    form = projForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio:index')
    
    return render(request, 'project/projForm.html', {'form': form})

def updateProj(request, projectId):
    project = Project.objects.get(id=projectId)
    form = projForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('portfolio:index')

    return render(request, 'project/projForm.html', {'form': form, 'project': project})

def deleteProj(request, projectId):
    project = Project.objects.get(id=projectId)

    if request.method == 'POST':
        project.delete()
        return redirect('portfolio:index')

    return render(request, 'project/projDelete.html', {'project': project})
