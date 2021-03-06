"""CS3620_Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import login, views as authenticationViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('hobbies/', include('hobby.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('contact/', include('contact.urls')),
    path('register/', userViews.register, name='Register'),
    path('login/',authenticationViews.LoginView.as_view(template_name = 'users/login.html'), name='Login'),
    path('logout/',authenticationViews.LogoutView.as_view(template_name = 'users/logout.html'), name='Logout'),

]
