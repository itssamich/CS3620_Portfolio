from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    aboutMe = ('Hello! I am Alex Klein, a current Senior at Weber State but this will be my last semester at ' 
            'Weber as I am transferring to UGA in the Spring to finish out my degree.\n I am interested in '
                        'Full Stack Web Development but I am not comfortable enough in any specific framework to work '
                        'on anything real at this time. I\'m pretty lost at what it is exactly I want to do, which '
                        'isn\'t a good look for a senior. But this is what I get for rushing through without thinking...')
    context = {'aboutMe':aboutMe}
    return render(request, 'home/index.html', context)

