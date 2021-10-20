from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ContactMsg

# Create your views here.
def index(request):
    
    form = ContactMsg(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('contact:index')
    
    return render(request, 'contact/index.html', {'form': form})
