from . import views
from django.urls import path

app_name = 'hobby'

urlpatterns = [
    #/hobbies/
    path('', views.index, name='index'),
    #/hobbies/1
    path('<int:hobbyId>', views.detail, name='detail'),
]