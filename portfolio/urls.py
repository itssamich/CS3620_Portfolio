from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:projectId>', views.detail, name='detail'),
    path('add', views.createProj, name='createProj'),
    path('update/<int:projectId>', views.updateProj, name='updateProj'),
    path('delete/<int:projectId>', views.deleteProj, name='deleteProj'),
]
