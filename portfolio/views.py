from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.template import loader

# Create your views here.
def index(request):
    projList = Project.objects.all()
    context = {
        'projList': projList,
    }
    return render(request, 'project/index.html', context)

