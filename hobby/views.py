from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from django.template import loader

# Create your views here.
def index(request):
    hobbyList = Hobby.objects.all()
    context = {
        'hobbyList': hobbyList,
    }
    return render(request, 'hobby/index.html', context)

def detail(request, hobbyId):
    hobby = Hobby.objects.get(pk=hobbyId)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobby/detail.html', context)