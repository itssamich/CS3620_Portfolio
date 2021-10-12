from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:projectId>', views.detail, name='detail'),
]
